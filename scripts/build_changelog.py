#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
from datetime import datetime
from typing import Any  # type: ignore[reportAny]

import requests


class Arguments(argparse.Namespace):
    def __init__(self) -> None:
        super().__init__()

        self.git_repo: str
        self.package: str
        self.revision: str
        self.build_version: str
        self.version: str
        self.date: str
        self.commit_hash: str
        self.status: str
        self.target: str
        self.urgency: str
        self.maintainer_name: str
        self.maintainer_email: str
        self.changelog: str


def parse_args() -> Arguments:
    parser = argparse.ArgumentParser()

    _ = parser.add_argument(
        "--git-repo",
        type=str,
        required=True,
        help="The git repo <git_service>/<user>/<repo>.git",
    )
    _ = parser.add_argument(
        "--revision",
        type=str,
        required=True,
        help="Package version",
    )
    _ = parser.add_argument(
        "--package",
        type=str,
        required=True,
        help="Package name",
    )
    _ = parser.add_argument(
        "--version",
        type=str,
        required=True,
        help="Version of the package from github release; can also be a commit hash",
    )
    _ = parser.add_argument(
        "--build-version",
        type=str,
        required=True,
        help="The build number",
    )
    _ = parser.add_argument(
        "--date",
        type=str,
        required=True,
        help="The build date",
    )
    _ = parser.add_argument(
        "--commit_hash",
        type=str,
        required=True,
        help="The commit hash",
    )
    _ = parser.add_argument(
        "--status",
        type=str,
        required=True,
        help="The package version status (e.g., stable, unstable)",
    )
    _ = parser.add_argument(
        "--target",
        type=str,
        required=True,
        help="The upload target",
    )
    _ = parser.add_argument(
        "--urgency",
        type=str,
        required=True,
        help="The upload target",
    )
    _ = parser.add_argument(
        "--maintainer-name",
        type=str,
        required=True,
        help="Name of the maintainer",
    )
    _ = parser.add_argument(
        "--maintainer-email",
        type=str,
        required=True,
        help="Email of the maintainer",
    )
    _ = parser.add_argument(
        "--changelog",
        type=str,
        required=True,
        help="Output path. Should be debian/changelog.",
    )

    return parser.parse_args(namespace=Arguments())


def get_last_release_info(repository: str) -> dict[str, Any]:
    url = f"https://api.github.com/repos/{repository}/releases"
    response = requests.get(url)

    releases: list[dict[str, Any]] = response.json()
    last_release: dict[str, Any] = releases[0]

    return last_release


def parse_changelog(changelog: str) -> str:
    md_sections = [
        r"^\# ",
        r"^\#\# ",
        r"^\#\#\# ",
        r"^\#\#\#\# ",
        r"^\#\#\#\#\# ",
        r"^\s*\* ",
        r"^\s*\- ",
    ]

    stats = [0] * len(md_sections)
    for sec, pattern in enumerate(md_sections):
        matches = re.findall(pattern, changelog, re.MULTILINE)
        if len(matches) > 0:
            stats[sec] = len(matches)

    first_level = 0
    for idx, s in enumerate(stats):
        if s > 0:
            first_level = idx
            break
    else:
        return changelog

    if first_level < len(md_sections) - 1:
        for l in range(first_level + 1, len(md_sections)):
            changelog = re.sub(
                md_sections[l],
                r"    - ",
                changelog,
                flags=re.MULTILINE,
            )

        changelog = re.sub(
            md_sections[first_level],
            r"  * ",
            changelog,
            flags=re.MULTILINE,
        )

    changelog = "\n".join(
        filter(
            lambda x: x.strip().startswith(("* ", "- ")),
            changelog.splitlines(),
        )
    )

    return changelog


def get_changelog_from_release(repository: str, version: str) -> str:
    last_release = get_last_release_info(repository)

    if version not in last_release["name"]:
        raise ValueError(
            f"Invalid version {version} for package {last_release['name']}"
        )

    changelog: str = last_release["body"]
    changelog = changelog.replace("\r", "")
    changelog = parse_changelog(changelog)

    if len(changelog) == 0:
        changelog = "  * updated package"

    return changelog


def extract_commit_form_version(version: str) -> str | None:
    pattern = r"\+git\d{8}\.([a-f0-9]+)"
    match = re.search(pattern, version)
    return match.group(1) if match else None


def get_version(
    version: str,
    revision: str,
    build_version: str,
    date: str,
    commit_hash: str,
    status: str,
) -> str:
    ver = f"{version}{build_version}"
    if commit_hash:
        ver += f"+git{date}.{commit_hash}"
    if status:
        ver += f"~{status}"
    ver += f"-{revision}"
    return ver


def format_debian_changelog(
    repository: str,
    package: str,
    version: str,
    revision: str,
    build_version: str,
    date: str,
    commit_hash: str,
    status: str,
    prev_version: str | None,
    target: str,
    urgency: str,
    maintainer_name: str,
    maintainer_email: str,
) -> str:
    crt_date = datetime.today().strftime("%a, %d %b %Y %H:%M:%S +0000")

    if commit_hash:
        cmd = ["git", "log", '--pretty="%h %s"']
        if prev_version:
            start_commit = extract_commit_form_version(prev_version)
            assert (
                start_commit is not None
            ), f"`start_commit` cannot be None: {prev_version}"

            if start_commit == commit_hash:
                changelog = "  * updated package"
                cmd = None
            else:
                cmd += [f"{start_commit}..{commit_hash}"]
        else:
            cmd += [f"{commit_hash}"]

        if cmd is not None:
            changelog = subprocess.run(cmd, capture_output=True).stdout
            changelog = changelog.decode("utf8")
            changelog = "\n".join(
                map(
                    lambda x: f"  * {x[1:-1]}",
                    filter(lambda x: len(x.strip()), changelog.split("\n")),
                )
            )
    else:
        changelog = get_changelog_from_release(repository, version)

    ver = get_version(version, revision, build_version, date, commit_hash, status)

    if ver == prev_version:
        raise RuntimeError("Version log already saved")

    deb_changelog = f"{package} ({ver}) {target}; urgency={urgency}\n\n"
    deb_changelog += f"{changelog}\n\n"
    deb_changelog += f" -- {maintainer_name} <{maintainer_email}>  {crt_date}\n"

    return deb_changelog


def get_prev_changelog(args: Arguments) -> tuple[str | None, str | None]:
    if not os.path.exists(args.changelog):
        return None, None

    contents = []
    version = None

    with open(args.changelog, "r") as file:
        contents = file.readlines()

        if len(contents) > 0:
            package, version, *_ = contents[0].split()
            if package != args.package:
                raise ValueError(f"Invalid package: {package}")

            version = version.replace("(", "").replace(")", "")

    return "".join(contents), version


def main(args: Arguments) -> None:
    contents, prev_version = get_prev_changelog(args)
    contents = "" if contents is None else contents

    try:
        debian_changelog = format_debian_changelog(
            args.git_repo,
            args.package,
            args.version,
            args.revision,
            args.build_version,
            args.date,
            args.commit_hash,
            args.status,
            prev_version,
            args.target,
            args.urgency,
            args.maintainer_name,
            args.maintainer_email,
        )
    except Exception as e:
        print(e)
        return

    with open(args.changelog, "w") as file:
        _ = file.write(debian_changelog)
        _ = file.write("\n")
        _ = file.write(contents)


if __name__ == "__main__":
    main(parse_args())

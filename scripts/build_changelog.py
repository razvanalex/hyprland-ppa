#!/usr/bin/env python3

import argparse
import re
import requests
import os
from datetime import datetime
from typing import Any  # type: ignore[reportAny]

class Arguments(argparse.Namespace):
    def __init__(self) -> None:
        super().__init__()

        self.github_repo: str
        self.package: str
        self.package_version: str
        self.build_version: str
        self.version: str
        self.target: str
        self.urgency: str
        self.maintainer_name: str
        self.maintainer_email: str
        self.changelog: str


def parse_args() -> Arguments:
    parser = argparse.ArgumentParser()

    _ = parser.add_argument(
        '--github-repo',
        '-r',
        type=str,
        required=True,
        help="The github repor <user>/<repo>",
    )
    _ = parser.add_argument(
        '--package-version',
        '-pv',
        type=str,
        required=True,
        help="Package version",
    )
    _ = parser.add_argument(
        '--package',
        '-p',
        type=str,
        required=True,
        help="Package name",
    )
    _ = parser.add_argument(
        '--version',
        '-v',
        type=str,
        required=True,
        help="Version of the package from github release",
    )
    _ = parser.add_argument(
        '--build-version',
        '-bv',
        type=str,
        required=True,
        help="The build number",
    )
    _ = parser.add_argument(
        '--target',
        '-t',
        type=str,
        required=True,
        help="The upload target",
    )
    _ = parser.add_argument(
        '--urgency',
        '-u',
        type=str,
        required=True,
        help="The upload target",
    )
    _ = parser.add_argument(
        '--maintainer-name',
        '-n',
        type=str,
        required=True,
        help="Name of the maintainer",
    )
    _ = parser.add_argument(
        '--maintainer-email',
        '-e',
        type=str,
        required=True,
        help="Email of the maintainer",
    )
    _ = parser.add_argument(
        '--changelog',
        '-c',
        type=str,
        required=True,
        help="Output path. Should be debian/changelog.",
    )

    return parser.parse_args(namespace=Arguments())


def get_last_release_info(repository: str) -> dict[str, Any]:
    url = f'https://api.github.com/repos/{repository}/releases'
    response = requests.get(url)

    releases: list[dict[str, Any]] = response.json()
    last_release: dict[str, Any] = releases[0]
    
    return last_release


def parse_changelog(changelog: str) -> str:
    md_sections = [
        r'^\# ',
        r'^\#\# ',
        r'^\#\#\# ',
        r'^\#\#\#\# ',
        r'^\#\#\#\#\# ',
        r'^\s*\* ',
        r'^\s*\- ',
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
                r'    - ',
                changelog,
                flags=re.MULTILINE,
            )

        changelog = re.sub(
            md_sections[first_level],
            r'  * ',
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


def format_debian_changelog(
    repository: str,
    package: str,
    version: str,
    package_version: str,
    build_version: str,
    target: str,
    urgency: str,
    maintainer_name: str,
    maintainer_email: str
) -> str:
    last_release = get_last_release_info(repository)
    crt_date = datetime.today().strftime('%a, %d %b %Y %H:%M:%S +0000')

    if version not in last_release['name']:
        raise ValueError(
            f"Invalid version {version} for package {last_release['name']}"
        )

    changelog: str = last_release['body']
    changelog = changelog.replace('\r', '')
    changelog = parse_changelog(changelog)

    if len(changelog) == 0:
        changelog = "  * updated package"

    deb_changelog = f"{package} ({version}{build_version}-{package_version}) {target}; urgency={urgency}\n\n"
    deb_changelog += f"{changelog}\n\n"
    deb_changelog += f" -- {maintainer_name} <{maintainer_email}>  {crt_date}\n"

    return deb_changelog


def main(args: Arguments) -> None:
    contents = []
    if os.path.exists(args.changelog):
        with open(args.changelog, "r") as file:
            contents = file.readlines()

            if len(contents) > 0:
                package, version, *_ = contents[0].split()
                if package != args.package:
                    raise ValueError(f"Invalid package: {package}")

                # NOTE: Make the assumption that versions only increase
                version, package_version = version.replace("(", "").replace(")", "").split('-')
                print("Found:", package, version, package_version)

                if version == args.version and package_version == args.package_version:
                    print("Changelog already written")
                    return

    debian_changelog = format_debian_changelog(
        args.github_repo,
        args.package,
        args.version,
        args.package_version,
        args.build_version,
        args.target,
        args.urgency,
        args.maintainer_name,
        args.maintainer_email
    )

    with open(args.changelog, 'w') as file:
        _ = file.write(debian_changelog)
        _ = file.write("\n")
        _ = file.write("".join(contents))


if __name__ == "__main__":
    main(parse_args())

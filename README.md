# hyprland-ppa

Custom Debian/Ubuntu packaging and Launchpad PPA automation for Hyprland ecosystem tools and desktop utilities.

Target distribution: **Ubuntu 26.04 (Resolute)**

## Prerequisites & Setup

### 1. Maintainer Identity

Package changelogs and source signatures require your maintainer identity. Set these via environment variables or define them in `.env` in the repository root:

```bash
export DEBFULLNAME="Your Name"
export DEBEMAIL="your.email@example.com"
```

> [!NOTE]
> If not explicitly exported, `DEBFULLNAME` and `DEBEMAIL` default to your `git config` values (`user.name` and `user.email`). `.env` is ignored by Git to prevent committing personal identities or local secrets.

### 2. GPG Signing & Hardware Keys

Package signing is delegated to your host's `gpg-agent`. When starting the build container, the host agent socket (`agent-extra-socket` or `agent-socket`) is mounted into the container along with `~/.gnupg` (read-only):

- **Hardware keys (YubiKey / smartcards)** work out of the box, pinentry prompts will trigger on your host.
- Ensure your signing key's email matches `DEBEMAIL`.

## Build Environment (Docker)

All package source generation and builds run inside an isolated Ubuntu build container.

### Build the Docker Container

```bash
# Full build environment (recommended)
make docker_build

# Minimal environment
make docker_build_minimal
```

### Enter the Container

```bash
# Launch interactive container shell with GPG agent forwarding
make docker_bash

# Or for minimal container:
make docker_bash_minimal
```

## Packaging Workflow

Inside the container (`make docker_bash`):

### 1. Build a Source Package

Navigate to the target package directory and run `make`:

```bash
cd ppa/<package-name>
make
```

This step:
1. Downloads upstream sources (release tarball or git commit).
2. Generates/updates `debian/changelog` and `debian/copyright` (using `decopy`).
3. Runs any package-specific prep (e.g., vendoring Rust dependencies offline for Launchpad compliance).
4. Runs `debuild -S` to generate a signed `.changes` and `.dsc` source package.

### 2. Test Build Locally (Optional)

To test build the `.deb` binary packages locally using container build dependencies:

```bash
cd ppa/<package-name>
make build_deb
```

### 3. Publish to Launchpad PPA

To upload the generated source package to the PPA via `dput`:

```bash
cd ppa/<package-name>
make publish
```

Target PPA: `ppa:razvanalex/hyprland-ppa` (configurable via `PPA` variable).

### 4. Clean Build Artifacts

```bash
cd ppa/<package-name>
make clean
```

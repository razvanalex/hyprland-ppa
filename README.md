# hyprland-ppa

## Build

Create the following files, and replace the placeholders:
* `.env`
``` bash
export DEBFULLNAME="YOUR NAME HERE"
export DEBEMAIL="YOUR EMAIL HERE"
```
* `.pgp`
```
YOUR PASSPHRASE HERE
```

> [!NOTE]
> These files are ignored from git to avoid leaking personal secrets.

To build a specific package, `cd` to that package and run `make`. Every time you need to rebuild the package, run `make clean`.

To publish the package on Launchpad, run `make publish`.


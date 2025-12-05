SHELL			:= /bin/bash
PACKAGE			:= swww
REPOSITORY		:= https://github.com/LGFae/swww.git
VERSION			:= 0.9.5
COMMIT_HASH		:= 004dfd8b
BUILD           :=
REVISION		:= 1
STATUS			:=
TARBALL_URL		:=
TARGET  		?= questing
URGENCY 		?= medium
DEBFULLNAME 	?=
DEBEMAIL    	?=
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/swww-unstable/

include $(ROOT)/Makefile.defs

# Because of limitations regarding networking when building rust packages on
# Launchpad, we need to include the dependencies in the archive. In addition,
# we need to allow binaries in the archive, otherwise build will fail.
prepare:
	cd $(BUILD_DIR) && \
	mkdir -p .cargo && \
	cargo vendor > .cargo/config.toml

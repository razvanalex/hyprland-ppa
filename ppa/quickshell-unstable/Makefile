SHELL			:= /bin/bash
PACKAGE			:= quickshell
REPOSITORY		:= https://git.outfoxxed.me/quickshell/quickshell.git
VERSION			:= 0.0.0
COMMIT_HASH		:= e649d24
BUILD           :=
REVISION		:= 1
STATUS			:=
TARBALL_URL		:=
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/quickshell-unstable/

include $(ROOT)/Makefile.defs

prepare:
	cd $(BUILD_DIR) && git submodule update --init --recursive

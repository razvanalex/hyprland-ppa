SHELL			:= /bin/bash
PACKAGE			:= satty
REPOSITORY		:= https://github.com/Satty-org/Satty.git
VERSION			:= 0.22.0
COMMIT_HASH		:=
BUILD           := d
REVISION		:= 1
STATUS			:=
TARBALL_URL		:= https://github.com/Satty-org/Satty/archive/refs/tags/v$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/satty/

include $(ROOT)/Makefile.defs

prepare:
	mv build/Satty-$(VERSION)/ $(BUILD_DIR)

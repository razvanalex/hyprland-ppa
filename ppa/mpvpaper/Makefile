SHELL			:= /bin/bash
PACKAGE			:= mpvpaper
REPOSITORY		:= https://github.com/GhostNaN/mpvpaper.git
VERSION			:= 1.7
COMMIT_HASH		:= 
BUILD           := d
REVISION		:= 1
STATUS			:=
TARBALL_URL		:= https://github.com/GhostNaN/mpvpaper/archive/refs/tags/$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/mpvpaper/

include $(ROOT)/Makefile.defs

prepare:
	mv build/mpvpaper-$(VERSION)/ $(BUILD_DIR)

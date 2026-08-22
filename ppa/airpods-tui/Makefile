SHELL			:= /bin/bash
PACKAGE			:= airpods-tui
REPOSITORY		:= https://github.com/annoyedmilk/airpods-tui.git
VERSION			:= 0.3.2
COMMIT_HASH		:=
BUILD           := d
REVISION		:= 1
STATUS			:=
TARBALL_URL		:= https://github.com/annoyedmilk/airpods-tui/archive/refs/tags/v$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
DEBFULLNAME 	?= Răzvan-Alexandru Smădu
DEBEMAIL    	?= razvansmadu@gmail.com
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/airpods-tui/

include $(ROOT)/Makefile.defs

prepare:
	mv build/airpods-tui-$(VERSION)/ $(BUILD_DIR)

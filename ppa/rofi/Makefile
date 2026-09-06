SHELL			:= /bin/bash
PACKAGE			:= rofi
VERSION			:= 1.7.5+wayland3
BUILD           := b
REVISION		:= 1
REPOSITORY		:= lbonn/rofi
TARBALL_URL		:= https://github.com/$(REPOSITORY)/releases/download/$(shell echo $(VERSION) | sed s/\+/%2B/g)/rofi-$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/$(PACKAGE)/

include $(ROOT)/Makefile.defs

prepare:
	mv build/rofi-$(VERSION)/ $(BUILD_DIR)

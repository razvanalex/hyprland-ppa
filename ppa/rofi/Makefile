SHELL			:= /bin/bash
PACKAGE			:= rofi
VERSION			:= 1.7.5+wayland3
BUILD           := a
PACKAGE_VERSION := 1
REPOSITORY		:= lbonn/rofi
TARBALL			:= https://github.com/$(REPOSITORY)/releases/download/$(shell echo $(VERSION) | sed s/\+/%2B/g)/rofi-$(VERSION).tar.gz
TARGET  		?= questing
URGENCY 		?= medium
DEBFULLNAME 	?=
DEBEMAIL    	?=
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/$(PACKAGE)/

include $(ROOT)/Makefile.defs

prepare:
	echo "Nothing to do"

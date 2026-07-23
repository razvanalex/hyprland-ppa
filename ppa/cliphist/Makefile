SHELL			:= /bin/bash
PACKAGE			:= cliphist
REPOSITORY		:= https://github.com/sentriz/cliphist.git
VERSION			:= 0.7.0
COMMIT_HASH		:= 
BUILD           := d
REVISION		:= 1
STATUS			:=
TARBALL_URL		:= https://github.com/sentriz/cliphist/archive/v$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
DEBFULLNAME 	?= Răzvan-Alexandru Smădu
DEBEMAIL    	?= razvansmadu@gmail.com
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/cliphist/

include $(ROOT)/Makefile.defs

prepare:
	mv build/cliphist-$(VERSION)/ $(BUILD_DIR)
	cd $(BUILD_DIR) && \
	GOPROXY=https://proxy.golang.org go mod vendor

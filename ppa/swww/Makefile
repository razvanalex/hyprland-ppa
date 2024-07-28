SHELL			:= /bin/bash
PACKAGE			:= swww
VERSION			:= 0.9.5
BUILD           := c
PACKAGE_VERSION := 1
REPOSITORY		:= LGFae/swww
TARBALL			:= https://github.com/$(REPOSITORY)/archive/refs/tags/v$(VERSION).tar.gz
TARGET  		?= noble
URGENCY 		?= medium
DEBFULLNAME 	?=
DEBEMAIL    	?=
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/$(PACKAGE)/

include $(ROOT)/Makefile.defs

# Because of limitations regarding networking when building rust packages on
# Launchpad, we need to include the dependencies in the archive. In addition,
# we need to allow binaries in the archive, otherwise build will fail.
prepare:
	cd build/$(PACKAGE)-$(VERSION)$(BUILD) \
	&& \
	mkdir -p .cargo \
	&& \
	cargo vendor > .cargo/config.toml \
	&& \
	( \
		cd .. && \
		rm -f $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz && \
		tar -czf $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz $(PACKAGE)-$(VERSION)$(BUILD) \
	)

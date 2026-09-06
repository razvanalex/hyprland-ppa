SHELL			:= /bin/bash
PACKAGE			:= ags
VERSION			:= 1.8.2
BUILD           := c
REVISION		:= 1
REPOSITORY		:= Aylur/ags
TARBALL_URL 	:= https://github.com/$(REPOSITORY)/releases/download/v$(VERSION)/$(PACKAGE)-v$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/$(PACKAGE)/
BUILD_ROOT		:= $(PACKAGE_ROOT)/build/

include $(ROOT)/Makefile.defs

prepare:
	mv build/$(PACKAGE) $(BUILD_DIR)
	cd $(BUILD_DIR) && \
	curl -LJO https://github.com/$(REPOSITORY)/releases/download/v$(VERSION)/node_modules-v$(VERSION).tar.gz && \
	tar xvf node_modules-v$(VERSION).tar.gz && \
	rm -fr node_modules-v$(VERSION).tar.gz && \
	npm install typescript --save-dev && \
	( \
		cd .. && \
		rm -f $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz && \
		tar -czf $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz $(PACKAGE)-$(VERSION)$(BUILD) \
	)

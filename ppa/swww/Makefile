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
PACKAGE_ROOT    := $(ROOT)/ppa/swww/

# Because of limitations regarding networking when building rust packages on
# Launchpad, we need to include the dependencies in the archive. In addition,
# we need to allow binaries in the archive, otherwise build will fail.
build: sign_pgp_init clean
	$(info Build $(PACKAGE) from release $(VERSION))
	mkdir -p build && cd build \
	&& \
	curl -LJ -o $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz $(TARBALL) \
	&& \
	tar xf $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz \
	&& \
	([ -n "$(BUILD)" ] && mv $(PACKAGE)-$(VERSION) $(PACKAGE)-$(VERSION)$(BUILD) || echo "skipping renaming") \
	&& \
	cd $(PACKAGE)-$(VERSION)$(BUILD) \
	&& \
	mkdir -p .cargo \
	&& \
	cargo vendor > .cargo/config.toml \
	&& \
	( \
		cd .. && \
		rm -f $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz && \
		tar -czf $(PACKAGE)_$(VERSION)$(BUILD).orig.tar.gz $(PACKAGE)-$(VERSION)$(BUILD) \
	) \
	&& \
	mkdir -p debian \
	&& \
	$(ROOT)/scripts/build_changelog.py \
		--github-repo $(REPOSITORY) \
		--package $(PACKAGE) \
		--version $(VERSION)$(BUILD) \
		--package-version $(PACKAGE_VERSION) \
		--build-version $(BUILD) \
		--target $(TARGET) \
		--urgency $(URGENCY) \
		--maintainer-name "$(DEBFULLNAME)" \
		--maintainer-email "$(DEBEMAIL)" \
		--changelog $(PACKAGE_ROOT)/debian/changelog \
	&& \
	cp -r $(PACKAGE_ROOT)/debian . \
	&& \
	decopy --root . --output ./debian/copyright --exclude ./debian/ --mode full \
	&& \
	debuild -S -k${DEBEMAIL} --source-option=--include-binaries \
	&& \
	echo "done"

# HACK: This is a hack to enable GPG inside a container. Otherwise, build fails
# because it couldn't sign the files.
.PHONY: sign_pgp_init 
sign_pgp_init:
	gpg --clearsign --passphrase-file $(ROOT)/.pgp --dry-run --pinentry-mode loopback $(ROOT)/README.md

.PHONY: publish
publish:
	dput $(PPA) ./build/$(PACKAGE)_$(VERSION)$(BUILD)-$(PACKAGE_VERSION)_source.changes

.PHONY: clean
clean:
	rm -fr build

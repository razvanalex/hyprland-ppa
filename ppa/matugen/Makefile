SHELL			:= /bin/bash
PACKAGE			:= matugen
REPOSITORY		:= https://github.com/InioX/matugen.git
VERSION			:= 4.1.0
COMMIT_HASH		:= 
BUILD           := e
REVISION		:= 1
STATUS			:=
TARBALL_URL		:= https://github.com/InioX/matugen/archive/refs/tags/v$(VERSION).tar.gz
TARGET			?= resolute
URGENCY 		?= medium
PPA				?= ppa:razvanalex/hyprland-ppa
ROOT			:= $(shell pwd)/../../
PACKAGE_ROOT    := $(ROOT)/ppa/matugen/

include $(ROOT)/Makefile.defs

prepare:
	mv build/matugen-$(VERSION)/ $(BUILD_DIR)
	cd $(BUILD_DIR) && \
	cargo vendor > .cargo-config && \
	mkdir -p .cargo && \
	mv .cargo-config .cargo/config.toml && \
	python3 -c 'import os, json; [ (d := json.load(open(p := os.path.join(r, ".cargo-checksum.json"))), [d["files"].pop(k) for k in list(d.get("files", {})) if k.endswith(".orig")], json.dump(d, open(p, "w"))) for r, _, f in os.walk("vendor") if ".cargo-checksum.json" in f ]'

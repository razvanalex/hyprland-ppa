SHELL			:= /bin/bash
PACKAGE			:= satty
REPOSITORY		:= https://github.com/Satty-org/Satty.git
VERSION			:= 0.22.0
COMMIT_HASH		:=
BUILD           := g
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
	cd $(BUILD_DIR) && \
	mkdir -p .cargo && \
	cargo vendor > .cargo/config.toml && \
	python3 -c 'import os, json; [ (d := json.load(open(p := os.path.join(r, ".cargo-checksum.json"))), [d["files"].pop(k) for k in list(d.get("files", {})) if k.endswith(".orig")], json.dump(d, open(p, "w"))) for r, _, f in os.walk("vendor") if ".cargo-checksum.json" in f ]' && \
	python3 -c 'p = "src/tools/crop.rs"; s = open(p).read(); open(p, "w").write(s.replace("&& let Some(crop) = &self.crop\n                    && crop.active =>", "&& matches!(&self.crop, Some(crop) if crop.active) =>"))'

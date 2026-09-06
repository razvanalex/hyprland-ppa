DOCKER_IMAGE	?= docker.io/razvanalex/hyprland-build
DOCKER_LABEL	?= latest
DOCKER_EXEC		?= docker

GPG_AGENT_SOCKET := $(shell gpgconf --list-dir agent-extra-socket 2>/dev/null || gpgconf --list-dir agent-socket 2>/dev/null)

.PHONY: docker_build
docker_build:
	$(DOCKER_EXEC) build -f Containerfile -t $(DOCKER_IMAGE):$(DOCKER_LABEL)

.PHONY: docker_build
docker_build_minimal:
	$(DOCKER_EXEC) build -f Containerfile.minimal -t $(DOCKER_IMAGE)-minimal:$(DOCKER_LABEL)

.PHONY: docker_bash
docker_bash:
	$(DOCKER_EXEC) run -it --rm \
		-v $(shell pwd):/build \
		-v ~/.gnupg:/root/.gnupg:ro \
		-v $(GPG_AGENT_SOCKET):/root/.gnupg/S.gpg-agent \
		-w /build \
		--user root \
		$(DOCKER_IMAGE):$(DOCKER_LABEL) \
		bash

.PHONY: docker_bash_minimal
docker_bash_minimal:
	$(DOCKER_EXEC) run -it --rm \
		-v $(shell pwd):/build \
		-v ~/.gnupg:/root/.gnupg:ro \
		-v $(GPG_AGENT_SOCKET):/root/.gnupg/S.gpg-agent \
		-w /build \
		--user root \
		$(DOCKER_IMAGE)-minimal:$(DOCKER_LABEL) \
		bash

# .PHONY: docker_push
# docker_push:
# 	$(DOCKER_EXEC) push $(DOCKER_IMAGE)

DOCKER_IMAGE	?= docker.io/razvanalex/hyprland-build
DOCKER_LABEL	?= latest
DOCKER_EXEC		?= docker

.PHONY: docker_build
docker_build:
	$(DOCKER_EXEC) build -f Containerfile -t $(DOCKER_IMAGE):$(DOCKER_LABEL)

.PHONY: docker_build
docker_build_minimal:
	$(DOCKER_EXEC) build -f Containerfile.minimal -t $(DOCKER_IMAGE)-minimal:$(DOCKER_LABEL)

.PHONY: docker_bash
docker_bash:
	$(DOCKER_EXEC) run -it --rm -v $(shell pwd):/build -v ~/.gnupg:/root/.gnupg $(DOCKER_IMAGE):$(DOCKER_LABEL) bash

.PHONY: docker_bash
docker_bash_minimal:
	$(DOCKER_EXEC) run -it --rm -v $(shell pwd):/build -v ~/.gnupg:/root/.gnupg $(DOCKER_IMAGE)-minimal:$(DOCKER_LABEL) bash

# .PHONY: docker_push
# docker_push:
# 	$(DOCKER_EXEC) push $(DOCKER_IMAGE)

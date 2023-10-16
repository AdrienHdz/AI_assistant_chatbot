DOCKER-COMPOSE ?= docker-compose

.PHONY: dc-up
dc-up: 
	$(DOCKER-COMPOSE) --file docker-compose/base.yaml up --build --remove-orphans
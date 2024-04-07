## Variables
YELLOW := \033[1;33m
NC := \033[0m

.PHONY: up
up:
	@echo "${YELLOW}Starting Hemagon:Tests...${NC}\n"
	@docker compose -f dev.docker-compose.yml up -d

.PHONY: pull
pull:
	@echo "${YELLOW}Update Hemagon containers:Tests...${NC}\n"
	@docker compose -f dev.docker-compose.yml pull

.PHONY: down
down:
	@echo "${YELLOW}Stopping Hemagon:Tests...${NC}\n"
	@docker compose -f dev.docker-compose.yml down --remove-orphans

.PHONY: logs
logs:
	@echo "${YELLOW}Start following Hemagon Pytest container logs:Tests...${NC}\n"
	@docker compose -f dev.docker-compose.yml logs -f pytest
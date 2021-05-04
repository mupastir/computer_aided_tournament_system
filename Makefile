.PHONY: docker-build \
		docker-start \
		docker-clean \


lint: ## linter
	flake8 . --count --exit-zero

mypy: ## mypy
	mypy --allow-redefinition aided_tournament_system || continue

file_to_black = .
black: ## isort and black
	isort $(file_to_black); black $(file_to_black)

docker-build: ## docker build
	docker build -t cats-backend .
docker-start: ## start all docker services
	(test -f ./envs/.env && test -f ./aided_tournament_system/config/settings/local.py) || (echo "check ./envs/.env and ./aided_tournament_system/config/settings/local.py exists" && exit 1)
	docker-compose -f ./aided_tournament_system/docker-compose-local.yaml up -d
docker-clean: ## docker cleanup
	docker-compose down && rm -rf .docker

help: ## Display help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
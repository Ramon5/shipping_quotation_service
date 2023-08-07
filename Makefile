# Makefile

.DEFAULT_GOAL:= help
.PHONY: help

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Formatters

format-black: ## run black (code formatter)
	@black src/ tests/

format-isort: ## run isort (imports formatter)
	@isort src/ tests/

format: format-black format-isort ## run all formatters

##@ Linters

lint-black: ## run black in linting mode
	@black src/ tests/ --check

lint-isort: ## run isort in linting mode
	@isort src/ tests/ --check

lint-flake8: ## run flake8 (code linter)
	@flake8 src/ tests/

lint: lint-black lint-isort lint-flake8 ## run all linters

##@ Testing

unit-tests: ## run pytest unit tests
	@pytest --doctest-modules tests/

unit-test-cov:
	@pytest --doctest-modules --cov=src --cov-report term-missing --cov-report=html

unit-test-cov-fail:
	@pytest -s -l -vvv tests/ --cov src/ --cov-fail-under=80 --cov-report xml --cov-report term:skip-covered

clean-cov:
	@rm -rf .coverage
	@rm -rf htmlcov
	@rm -rf pytest.xml
	@rm -rf pytest-coverage.txt

export_requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt

###@ Run application

run: ## run application containers
	docker-compose up

initial_load:
	docker-compose run api python -m src.scripts.initial_load

SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy airbnbcrawl tests
	poetry run flake8 .
	poetry run doc8 -q docs

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

.PHONY: run
run:
	poetry run python airbnbcrawl/main.py

.DEFAULT:
	@cd docs && $(MAKE) $@


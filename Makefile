.PHONY: environment lint test
$(VERBOSE).SILENT:

EXECUTOR = poetry run

## Install (or update) Python environment
environment:
	poetry install; pre-commit install

## Inspect the code style using Flake8
lint:
	$(EXECUTOR) flake8 --max-line-length=120 --benchmark

## Test the exercises using Pytest
test:
	$(EXECUTOR) pytest

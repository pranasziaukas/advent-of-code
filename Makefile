.PHONY: environment lint test solution
$(VERBOSE).SILENT:

EXECUTOR = poetry run

## Install (or update) Python environment
environment:
	poetry install; pre-commit install

## Inspect the code style using Flake8
lint:
	$(EXECUTOR) flake8 --max-line-length=120 --extend-ignore=E203 --benchmark

## Test the exercises using Pytest
test:
	$(EXECUTOR) pytest

## Create a day folder based on the template, day=<number>
solution:
	cp -r .day_template day$$day &&\
	sed -i '' '/^version/s|2023.[0-9][0-9].[0-9]|2023.'$$day'.0|' pyproject.toml

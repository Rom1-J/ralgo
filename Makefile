VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python


.PHONY: main
main:
	/bin/python -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip install -U pip setuptools

.PHONY: install
install:
	$(VIRTUAL_ENV)/bin/pip install .

.PHONY: install-dev
install-dev:
	$(VIRTUAL_ENV)/bin/pip install -r dev.requirements.txt

.PHONY: update
update:
	$(VIRTUAL_ENV)/bin/pip install --upgrade .

.PHONY: update-all
update-all:
	$(VIRTUAL_ENV)/bin/pip install --upgrade --force-reinstall .

.PHONY: lint
lint:
	$(PYTHON_PATH) -m black `git ls-files "*.py"` --line-length=79 && $(PYTHON_PATH) -m pylint ralgo

.PHONY: test
test:
	$(PYTHON_PATH) -m pytest --durations=0

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy ralgo

.PHONY: coverage
coverage:
	$(PYTHON_PATH) -m coverage run -m pytest --durations=0
	$(PYTHON_PATH) -m coverage report -m
	$(PYTHON_PATH) -m coverage html
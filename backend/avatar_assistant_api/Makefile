.PHONY: install
install:
	pip install --upgrade pip &&\
	{ pip freeze | grep pip-tools > /dev/null || pip install pip-tools ; } &&\
	pip-compile requirements/requirements.in &&\
	pip-sync requirements/requirements.txt
	pre-commit install

.PHONY: format
format:
	find api -type f -name '*.py' -exec black {} +

.PHONY: lint
lint:
	find api -type f -name '*.py' -exec ruff check {} +

.PHONY: refactor
refactor: lint  format
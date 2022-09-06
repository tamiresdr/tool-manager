init-dev: install-dependencies

run:
	@poetry run python tool_manager/main.py

update: poetry.lock
	@poetry update

install-dependencies:
	@poetry install

bandit:
	@poetry run bandit -r -f custom app

mypy:
	@poetry run mypy tool_manager/

flake8:
	@poetry run flake8 tool_manager/ tests/

isort-check:
	@poetry run isort -c --profile=black -l 120 .

isort:
	@poetry run isort --profile=black -l 120 .

blue:
	@poetry run blue .

blue-check:
	@poetry run blue --check .

lint: isort blue

lint-check: mypy flake8 isort-check blue-check bandit

migrate:
	@poetry run python db/migrate.py

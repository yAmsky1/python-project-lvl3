install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

page-loader:
	poetry run page_loader

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=page-loader --cov-report xml

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

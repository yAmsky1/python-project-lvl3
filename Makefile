install:
	poetry install

build:
	poetry build

publish:
	poetry publish --drt-run

lint:
	poetry run flake8 page-loader

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=page-loader --cov-report xml

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

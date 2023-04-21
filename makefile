ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS))

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -e .[test]

pytest:
	pytest . --capture=no -vv

pytest_codecov:
	pytest \
		--junitxml=test-reports/junit.xml \
		--cov-config=.coveragerc \
		--cov-report=term \
		--cov=. \
		--codecov \
		$(ARGUMENTS)

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$DIRECTORY_PYPI_USERNAME --password $$DIRECTORY_PYPI_PASSWORD dist/*

# configuration for black and isort is in pyproject.toml
autoformat:
	isort $(PWD)
	black $(PWD)

checks:
	isort $(PWD) --check
	black $(PWD) --check --verbose
	flake8 .

.PHONY: clean test_requirements flake8 pytest publish autoformat checks

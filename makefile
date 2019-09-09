ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS))

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -e .[test]

flake8:
	flake8 . --exclude=.venv --max-line-length=120

pytest:
	pytest $(ARGUMENTS) --cov=. -v

publish:
	rm -rf build dist; \
	python setup.py bdist_wheel; \
	twine upload --username $$DIRECTORY_PYPI_USERNAME --password $$DIRECTORY_PYPI_PASSWORD dist/*

.PHONY: clean test_requirements flake8 pytest publish

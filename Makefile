setup:
		pipenv install --dev
			PIP_INSTALL_OPTION="-- -VERBOSITY=-1" pipenv run pre-commit install --hook-type pre-commit
			PIP_INSTALL_OPTION="-- -VERBOSITY=-1" pipenv run pre-commit install --hook-type pre-push


install:
		pipenv install --dev


format: 
		pipenv run pre-commit run black


shell: 
		pipenv shell


lint: 
		pipenv run mypy src


clean:
		pipenv --rm


.PHONY: install shell lint test clean # explicitly saying that we don't expect a file to be produced
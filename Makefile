watch:
	make -C docs livehtml

deps:
	pipenv install --dev --skip-lock

develop:
	pipenv run python setup.py develop

%:
	make -C docs $@

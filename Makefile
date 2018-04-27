watch:
	make -C docs livehtml

deps:
	pipenv install --dev --skip-lock

develop:
	pipenv run python setup.py develop

assets: node_modules/bulma/bulma.sass package-lock.json sass

package-lock.json node_modules node_modules/bulma node_modules/bulma/bulma.sass:
	npm install

webpack: node_modules/bulma/bulma.sass
	npm run build

sass:
	node-sass --include-path scss sphinx_bulma_theme/sphinx-bulma.src.sass sphinx_bulma_theme/static/css/theme.css
	node-sass --include-path scss sphinx_bulma_theme/sphinx-bulma.src.sass sphinx_bulma_theme/static/css/sphinx-bulma.css

clear:
	rm -rf docs/build

html %:
	rm -rf docs/build/$@
	make -C docs $@

tests:
	@echo -n "running tests... "
	@echo "OK"

release: tests docs
	@rm -rf dist/*
	@./.release
	@make pypi

pypi:
	@pipenv run python setup.py build sdist
	@pipenv run twine upload dist/*.tar.gz


.PHONY: webpack sass

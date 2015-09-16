all: helpers docs

helpers:
	python3 build.py

docs:
	pandoc -o README.rst README.md

upload:
	python setup.py sdist upload
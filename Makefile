install:
	poetry install
	poetry run brain-games
	build
	publish
	package-install
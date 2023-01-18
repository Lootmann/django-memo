run:
	python3 manage.py runserver

.PHONY: tailwind
tailwind:
	python3 manage.py tailwind start

.PHONY: test
test:
	pytest -sv

req:
	pip freeze > requirements.txt

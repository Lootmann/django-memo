run:
	python3 manage.py runserver

.PHONY: tailwind
tailwind:
	python3 manage.py tailwind start

req:
	pip freeze > requirements.txt

all: start

start:
	docker build -t my-django-app .
	docker run --name my-container -p 8000:8000 my-django-app

stop:
	docker stop my-container
	docker rm my-container
	docker rmi my-django-app

linter:
	pylint --rcfile lint/pylintrc project --ignore=settings.py

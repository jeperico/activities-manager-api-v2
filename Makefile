dockerup:
	sudo docker compose -f docker-compose.yml up -d --build

dockerdown:
	sudo docker compose -f docker-compose.yml down

migrate:
	python3 app/manage.py migrate

makemigrations:
	python3 app/manage.py makemigrations

runserver:
	python3 app/manage.py runserver

createsuperuser:
	python3 app/manage.py createsuperuser

pyshell:
	python3 app/manage.py shell

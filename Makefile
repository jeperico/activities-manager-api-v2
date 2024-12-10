docker up:
	sudo docker compose -f docker-compose.yml up -d --build

docker down:
	sudo docker compose -f docker-compose.yml down

migrate:
	python3 app/manage.py migrate

makemigrations:
	python3 app/manage.py makemigrations

runserver:
	python3 app/manage.py runserver
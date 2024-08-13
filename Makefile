up:
	docker-compose.yml up -d

down:
	docker-compose.yml down && docker network prune --force

run:
	python manage.py runserver

worker: 
	celery -A crypto_tracker worker -l info

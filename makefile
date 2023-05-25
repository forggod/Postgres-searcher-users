.PHONY: test build up down

test:
	docker-compose up -d db_app
	docker-compose up app

build:
	sudo docker-compose build

# up:
# 	docker-compose up -d db_app
# 	docker-compose up -d app

down:
	docker-compose down

remove:
	docker-compose down --remove-orphans
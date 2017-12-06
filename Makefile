# Commands for the prod server
cleanup:
	rm -rf chordifyme_data/*

fetch-master: cleanup
	git pull origin master

build: cleanup
	docker-compose build $(container)
	docker-compose up -d $(container)

remove: cleanup
	docker-compose stop $(container)
	docker-compose rm -f $(container)

rebuild: cleanup remove build

rebuild-master: cleanup fetch-master remove build

# Commands for local development
build-local: cleanup
	docker-compose -f dev.yml build $(container)
	docker-compose -f dev.yml up -d $(container)

remove-local: cleanup
	docker-compose -f dev.yml stop $(container)
	docker-compose -f dev.yml rm -f $(container)

rebuild-local: cleanup remove-local build-local

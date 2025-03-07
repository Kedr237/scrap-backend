up:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans

stop:
	docker compose -f docker-compose.yml stop

rm:
	dcoker compose -f docker-compose.yml down

logs:
	docker compose -f docker-compose.yml logs

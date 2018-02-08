help:
	@echo "    docker-bash <container-name>"
	@echo "        Opens a shell session on the running container."

docker-bash:
	docker exec -i -t ${name} /bin/bash
help:
	@echo "    run-cmdline"
	@echo "        Run the bot in the command line."
	@echo "    train"
	@echo "        Train a combined Rasa NLU and Core model."

train:
	rasa train

run-actions:
	rasa run actions --actions actions.actions

run-cmdline:
	make run-actions &
	rasa run --endpoints endpoints.yml --enable-api -m models --debug

run-x:
	make run-actions &
	export RASA_X_PASSWORD=test &
	rasa x -m models --endpoints endpoints.yml

run-debug:
	make run-actions &
	export RASA_X_PASSWORD=test &
	rasa x -m models --endpoints endpoints.yml --debug

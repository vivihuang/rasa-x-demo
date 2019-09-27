help:
	@echo "    run-cmdline"
	@echo "        Run the bot in the command line."
	@echo "    train"
	@echo "        Train a combined Rasa NLU and Core model."

train:
	rasa train --fixed-model-name model

run-cmdline:
	rasa run actions --actions actions.actions &
	rasa run --endpoints endpoints.yml --enable-api -m models --debug

run-x:
	rasa run actions --actions actions.actions &
	export RASA_X_PASSWORD=test;
	rasa x -m models --endpoints endpoints.yml

run-debug:
	rasa run actions --actions actions.actions &
	export RASA_X_PASSWORD=test;
	rasa x -m models --endpoints endpoints.yml --debug

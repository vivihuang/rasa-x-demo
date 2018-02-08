import logging
import os

from rasa_core.channels.rest import HttpInputChannel
from rasa_extensions.core.remote import run_with_remote_core

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")

    model_dir = "models/dialogue"

    # instantiate the input channel you want to connect to
    from rasa_extensions.core.channels.rasa_chat import RasaChatInput

    input_channel = HttpInputChannel(
            5001, "/", RasaChatInput(os.environ.get("RASA_API_ENDPOINT_URL")))

    run_with_remote_core(model_dir,
                         "http://localhost:5005",
                         "",
                         input_channel)

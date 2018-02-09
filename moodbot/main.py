from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import time

from rasa_core.channels.rest import HttpInputChannel
from rasa_extensions.core.remote import run_with_remote_core

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")

    logger.info("Starting App")

    model_dir = "models/dialogue"

    # instantiate the input channel you want to connect to
    from rasa_extensions.core.channels.rasa_chat import RasaChatInput

    input_channel = HttpInputChannel(
            5001, "/", RasaChatInput(os.environ.get("RASA_API_ENDPOINT_URL")))

    time.sleep(5)
    run_with_remote_core(model_dir,
                         os.environ.get("RASA_REMOTE_CORE_ENDPOINT_URL"),
                         os.environ.get("RASA_CORE_TOKEN"),
                         input_channel)

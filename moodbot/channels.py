from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import requests
from flask import Blueprint, request, jsonify, abort
from flask_cors import CORS, cross_origin

from rasa_core.channels import UserMessage
from rasa_core.channels.rest import HttpInputComponent
from rasa_extensions.core.channels.nop import NOPChannel

logger = logging.getLogger(__name__)


class RasaChatInput(HttpInputComponent):
    def __init__(self, platform_api):
        self.platform_api = platform_api

    def blueprint(self, on_new_message):
        rasa_chat = Blueprint('rasa_chat', __name__)
        CORS(rasa_chat)

        @rasa_chat.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @rasa_chat.route("/send", methods=['GET', 'POST'])
        @cross_origin()
        def receive():
            user = fetch_user(self.platform_api, request)
            msg = request.json["message"]
            if user.get("role") == "admin":
                conversation_id = request.args.get("conversation",
                                                   user["user"])
            else:
                conversation_id = user["user"]
            on_new_message(UserMessage(msg, NOPChannel(),
                                       sender_id=conversation_id))

            return jsonify({"status": "ok"})

        return rasa_chat


def check_token(platform_host, headers):
    url = "{}/users/me".format(platform_host)
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        return result.json()
    else:
        logger.info("Failed to check token: {}. "
                    "Content: {}".format(token, request.data))
        return None


def fetch_user(platform_host, req):
    user = None
    if req.headers.get("Authorization"):
        headers = {"Authorization": req.headers.get("Authorization")}
        user = check_token(platform_host, headers)
    if user:
        return user

    abort(401)

ARG CORE_SDK_VERSION=1.3.3
FROM rasa/rasa-sdk:$CORE_SDK_VERSION

ENV RASA_X_PASSWORD test

RUN apt-get update
RUN apt-get install -y lsof curl vim

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5002

RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]

CMD ["start", "--actions", "actions.actions"]

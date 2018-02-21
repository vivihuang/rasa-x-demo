FROM python:2.7-slim

SHELL ["/bin/bash", "-c"]

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  openssh-client \
  graphviz-dev \
  pkg-config \
  git-core \
  openssl \
  libssl-dev \
  libffi6 \
  libffi-dev \
  libpng12-dev \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  mkdir /app

WORKDIR /app

ARG RASA_PYPI_USER
ARG RASA_PYPI_PASSWORD

# Copy as early as possible so we can cache ...
COPY requirements.txt ./

# we use the Rasa python repository, as there are dependencies that are
# private. any public dependency is still fetched from pypi.python.org
RUN pip install  \
  -i "https://$RASA_PYPI_USER:$RASA_PYPI_PASSWORD@pypi.rasa.ai/simple/" \
  -r requirements.txt

COPY . /app

EXPOSE 5001

CMD ["python", "main.py"]
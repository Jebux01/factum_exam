FROM python:3.9-slim as builder

WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get clean \
  && apt-get -y install libpq-dev curl
COPY requirements.txt /tmp/requirements.txt

RUN pip install pip --upgrade && pip install -r /tmp/requirements.txt

RUN pwd

COPY . ./
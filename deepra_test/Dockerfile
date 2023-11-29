# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

COPY ./requirements.txt /backend/requirements.txt

RUN  python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

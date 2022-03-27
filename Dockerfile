FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /test_app

COPY  . .
COPY /requirements.txt .
RUN pip install -r requirements.txt

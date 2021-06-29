FROM python:3.7-slim-buster

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY ./ /usr/src/app

EXPOSE 5001
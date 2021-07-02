FROM python:3.7-slim-buster

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
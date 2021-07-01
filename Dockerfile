FROM python:3.7-slim-buster

COPY ./ /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /usr/src/app/dockerInit/
ENTRYPOINT ["/usr/src/app/dockerInit/docker-entrypoint.sh"]
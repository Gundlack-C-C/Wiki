FROM python:3.7-slim-buster

COPY ./ /usr/src/app
COPY ./requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]

EXPOSE 5001
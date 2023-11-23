FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

WORKDIR /script

COPY . .

CMD [ "python", "script.py" ]

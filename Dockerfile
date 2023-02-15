FROM python:3.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

RUN python-on-whales download-cli

COPY . /app
WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]

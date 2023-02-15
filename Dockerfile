FROM python:3.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

RUN apt update
RUN apt install -y docker.io
RUN apt-get clean all
RUN rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]

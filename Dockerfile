FROM python:3.11.0a7-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]

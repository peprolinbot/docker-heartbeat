FROM python:3.9.10-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]

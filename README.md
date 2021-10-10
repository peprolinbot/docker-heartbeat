# docker-heartbeat

Api to do a _heartbeat_ (is it running?) check on your docker containers.

## 🔧 How to Install

### 🐳 Docker (Recommended)

If you are using this to check Docker containers, you probably like Docker. This is really easy to setup.

So the command is:
 
```bash
docker run -d --restart always --name docker-heartbeat -v /var/run/docker.sock:/var/run/docker.sock:ro \
    -p 8000:8000 \
    ghcr.io/peprolinbot/docker-heartbeat
```

#### Environment Variables

| Name                         | Description |
|------------------------------|-------------|
| `DHB_AVALIABLE_STAUS_CODE`   | Status code to give when the container is running.
| `DHB_UNAVALIABLE_STAUS_CODE` | Status code to give when the container is NOT running.
| `DHB_NOT_FOUND_STATUS_CODE`  | Status code to give when the container doesn't exist


#### Build the image

```bash
git clone https://github.com/peprolinbot/docker-heartbeat.git
cd docker-heartbeat
docker build -t docker-heartbeat .
```

### 💪🏻 Without Docker

```bash
git clone https://github.com/peprolinbot/docker-heartbeat.git
cd docker-heartbeat
python3 main.py # For development
# OR
gunicorn main:app -b 0.0.0.0:8000 # For production
```

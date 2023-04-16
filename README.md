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
| `DHB_AVALIABLE_STATUS_CODE`   | Status code to give when the container is running. _(Default: 200)_
| `DHB_UNAVALIABLE_STATUS_CODE` | Status code to give when the container is NOT running. _(Default: 503)_
| `DHB_NOT_FOUND_STATUS_CODE`  | Status code to give when the container doesn't exist. _(Default: 404)_


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

## ⚡ API Docs

### Quick start

To check a container's status you can go to `http://127.0.0.1:8000/container/<container_name_or_id>`

It will return the specified status code and a JSON output. This also works for services and stacks on their respectives endpoints. (`/service/<foo>` and `/stack/<bar>`)

### Endpoints

Below are the expected JSON output for every endpoint. If the _thing_ you are querying isn't found. It'd be `{"error":"(Container/Service/Stack) not found"}`

- /container/<container_name_or_id>
```
{
    "status":"running"
}
```
- /service/<service_name_or_id>
```
{
    "status": {"0": "running",
               "1": "running",
               "2": "running"}
}
```

- /stack/<stack_name_or_id>
```
{
    "status": {"mystack_app": {"0": "running",
                               "1": "running",
                               "2": "running"},
               "mystack_proxy": {"0": "running"},
               "mystack_database": {"0": "running",
                                    "1": "running"}
}            
```

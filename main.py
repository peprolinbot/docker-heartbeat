import os
import docker
from flask import Flask

AVALIABLE_STAUS_CODE = os.environ.get('DHB_AVALIABLE_STAUS_CODE', 200)
UNAVALIABLE_STAUS_CODE = os.environ.get('DHB_UNAVALIABLE_STAUS_CODE', 503)
NOT_FOUND_STATUS_CODE = os.environ.get('DHB_NOT_FOUND_STATUS_CODE', 404)

docker_client = docker.from_env()

app = Flask(__name__)

@app.route('/container/<id_or_name>')
def get_container_status(id_or_name):
    try:
        container = docker_client.containers.get(id_or_name)
    except docker.errors.NotFound:
        output = {"error": "Container not found"}
        status_code = NOT_FOUND_STATUS_CODE
    else:
        status = container.status
        output = {"status": status}
        if output.get("status") == "running":
            status_code = AVALIABLE_STAUS_CODE
        else:
            status_code = UNAVALIABLE_STAUS_CODE
    return output, status_code



if __name__ == '__main__':
    app.run(host='0.0.0.0')

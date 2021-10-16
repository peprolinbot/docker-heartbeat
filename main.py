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
        status = NOT_FOUND_STATUS_CODE
    else:
        output = {"status": container.status}
        if output.get("status") == "running":
            status = AVALIABLE_STAUS_CODE
        else:
            status = UNAVALIABLE_STAUS_CODE
    return output, status



if __name__ == '__main__':
    app.run(host='0.0.0.0')

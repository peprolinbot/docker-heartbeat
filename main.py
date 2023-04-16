from flask import Flask
import os
import docker
from python_on_whales import docker as pow_docker

AVALIABLE_STATUS_CODE = os.environ.get('DHB_AVALIABLE_STATUS_CODE', 200)
UNAVALIABLE_STATUS_CODE = os.environ.get('DHB_UNAVALIABLE_STATUS_CODE', 503)
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
            status_code = AVALIABLE_STATUS_CODE
        else:
            status_code = UNAVALIABLE_STATUS_CODE
    return output, status_code


@app.route('/service/<id_or_name>')
def get_service_status(id_or_name):
    try:
        service = docker_client.services.get(id_or_name)
    except docker.errors.NotFound:
        output = {"error": "Service not found"}
        status_code = NOT_FOUND_STATUS_CODE
    else:
        status_code = UNAVALIABLE_STATUS_CODE
        output = {"status": {}}
        for i, task in enumerate(service.tasks()):
            output["status"][i] = status = task["Status"]["State"]
            if status == "running":
                status_code = AVALIABLE_STATUS_CODE
    return output, status_code


@app.route('/stack/<id_or_name>')
def get_stack_status(id_or_name):
    services = pow_docker.stack.services(id_or_name)
    if not services:
        output = {"error": "Stack not found"}
        status_code = NOT_FOUND_STATUS_CODE
    else:
        status_code = AVALIABLE_STATUS_CODE
        output = {"status": {}}
        for service in services:
            _output, _status_code = get_service_status(service.id)
            output["status"][service.spec.name] = _output["status"]
            if _status_code != AVALIABLE_STATUS_CODE:
                status_code = _status_code
    
    return output, status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0')

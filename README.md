# Flask App Deployable to K8s

A simple webapp build with flask framework to be deployable into a kubernetes cluster.

**Note:**
The loadbalancer service is for local purpose. However, we could have used the default ClusterIP service insted of the loadbalancer and build an **ingress object** for the external connections.

## Deployment

1. Build the webapp image
    - run the **build** script in [app](./app/build)
2. Create its deployment object and its service
3. Check your localhost at 4001 port
    - curl localhost:4001

### Steps from root project path

```sh
docker build -t my-flask-web:0.0.1 ./app
kubectl create -f .k8s
```

---

## Environments

Local:
- root project path: **app/src/**
Tests:
 - path: **app/src/tests**


### [Local] Development process

1. Place youself at src path as the root flask project
    - ```cd app/src/```
2. Create your **venv** or favourite package manager (like poetry)
    - ```pip install -r requirements.txt```
3. Load all its dependencies (requirements.txt)
    - ```pip install -r requirements.txt```
4. Happy dev!    


Reminder:
- Any not-needed file or script for production must be ignored to our Dockerfile. This can be done creating a **.dockerignore** in our root flask project path.

### Tests

1. Place youself at src path as the root flask project
    - ```cd app/src/```
2. Load all its dependencies (requirements.txt)
    - ```pip install -r requirements.txt```
3. Run it

```sh
# All the tests
python -m pytest  tests
# Specific ones
$ python -m pytest -s tests/test_client.py
```

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

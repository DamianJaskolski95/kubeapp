# Introduction
This code was made with help of [this](https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes/kubernetes_deploy/) tutorial.

# How to run on local
1. Setup minikube
2. Build image
```
cd ./code
docker build -t damian/fastapikube .
```
3. Apply kubernetes infrastructure
```kubernetes
kubectl apply -f ./k8s/namespace -f ./postgres -f ./job -f ./code -f ./nginx
```
4. Start service to access from web browser
```
minikube service nginx-service -n fastapikube-project
```

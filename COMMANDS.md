# Useful commands

## kubectl
- `kubectl apply -k <directory-path>`: apply kustomization, do rolling update
- `kubectl rollout status deployment <deployment-name>`: monitor the status of rolling update
- `kubectl rollout undo deployment <deployment-name>`: rollback rolling update to previous revision
- `kubectl rollout undo deployment <deployment-name> --to-revision=1`: rollback rolling update to revision 1
- `kubectl run -it --rm debug --image=alpine --restart=Never -n development sh` -> `apk add --no-cache curl` login to interactive shell pod (with apache), add curl to for example test connectivity of ClusterIP
- `kubectl config set-context --current --namespace=development`: set default namespace for kubectl to development
- `kubectl get svc -A --field-selector spec.type=LoadBalancer`: get services from all namespaces, filter by service type
- `kubectl exec -it <pod-id> -- /bin/sh`: get interactive shell in a pod 

## minikube
- `minikube service <service-name>`: create a tunnel to expose service
- `minikube image load <image-name>`: copy image built locally to minikube
- `minikube addons enable ingress`: enable and start ingress controller before creating rules

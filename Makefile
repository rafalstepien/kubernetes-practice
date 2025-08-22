# apply-dev:
# 	kubectl apply -k manifests/dev

# expose-dev:
# 	minikube service dev-load-balancer -n development

# cleanup-dev:
# 	kubectl delete -k manifests/dev


# apply-prod:
# 	kubectl apply -k manifests/prod

# expose-prod:
# 	minikube service prod-load-balancer -n production

# cleanup-prod:
# 	kubectl delete -k manifests/prod



build:
	docker build -t info-backend:0.1.0 applications/info-backend
	docker build -t calculator-api:0.1.0 applications/calculator-api
	docker build -t calculator-backend:0.1.0 applications/calculator-backend

load:
	minikube image load info-backend:0.1.0
	minikube image load calculator-api:0.1.0
	minikube image load calculator-backend:0.1.0

apply-dev:
	kubectl apply -k manifests/dev
	kubectl apply -f manifests/dev/ingress-load-balancer.yaml

expose-dev:
	minikube service ingress-load-balancer -n ingress-nginx --url

cleanup-dev:
	kubectl delete -k manifests/dev
	kubectl delete -f manifests/dev/ingress-load-balancer.yaml

minikube-image-cleanup:
	minikube image rm docker.io/library/info-backend:0.1.0
	minikube image rm docker.io/library/calculator-api:0.1.0
	minikube image rm docker.io/library/calculator-backend:0.1.0
build:
	docker build -t info-backend:0.1.0 applications/info-backend
	docker build -t calculator-api:0.1.0 applications/calculator-api
	docker build -t calculator-backend:0.1.0 applications/calculator-backend

load:
	minikube image load info-backend:0.1.0
	minikube image load calculator-api:0.1.0
	minikube image load calculator-backend:0.1.0


image-cleanup:
	minikube image rm docker.io/library/info-backend:0.1.0
	minikube image rm docker.io/library/calculator-api:0.1.0
	minikube image rm docker.io/library/calculator-backend:0.1.0


apply-dev:
	kubectl apply -k manifests/dev

cleanup-dev:
	kubectl delete -k manifests/dev

apply-prod:
	kubectl apply -k manifests/prod

cleanup-prod:
	kubectl delete -k manifests/prod

apply-lb:
	kubectl apply -f manifests/ingress-load-balancer.yaml

cleanup-lb:
	kubectl delete -f manifests/dev/ingress-load-balancer.yaml

expose:
	sudo minikube tunnel

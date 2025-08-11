apply-dev:
	kubectl apply -k manifests/engine/dev
	kubectl apply -k manifests/api/dev

apply-prod:
	kubectl apply -k manifests/engine/prod
	kubectl apply -k manifests/api/prod

apply-all: apply-dev apply-prod

expose-dev:
	minikube service dev-load-balancer

expose-prod:
	minikube service prod-load-balancer

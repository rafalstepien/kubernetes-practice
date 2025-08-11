apply-dev:
	kubectl apply -k manifests/engine/dev
	kubectl apply -k manifests/api/dev

expose-dev:
	minikube service dev-load-balancer

cleanup-dev:
	kubectl delete -k manifests/api/dev
	kubectl delete -k manifests/engine/dev


apply-prod:
	kubectl apply -k manifests/engine/prod
	kubectl apply -k manifests/api/prod


expose-prod:
	minikube service prod-load-balancer


cleanup-prod:
	kubectl delete -k manifests/api/prod
	kubectl delete -k manifests/engine/prod



apply-all: apply-dev apply-prod
cleanup-all: cleanup-dev cleanup-prod
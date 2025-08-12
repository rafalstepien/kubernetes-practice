apply-dev:
	kubectl apply -k manifests/dev

expose-dev:
	minikube service dev-load-balancer -n development

cleanup-dev:
	kubectl delete -k manifests/dev


apply-prod:
	kubectl apply -k manifests/prod

expose-prod:
	minikube service prod-load-balancer -n production

cleanup-prod:
	kubectl delete -k manifests/prod

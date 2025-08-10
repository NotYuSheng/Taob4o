.PHONY: build up down logs clean

# Docker Compose commands
build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

clean:
	docker compose down -v
	docker system prune -f

# Kubernetes commands
k8s-deploy:
	kubectl apply -f k8s/

k8s-delete:
	kubectl delete -f k8s/

# Istio commands
istio-install:
	istioctl install --set values.defaultRevision=default -y
	kubectl label namespace default istio-injection=enabled

istio-deploy:
	kubectl apply -f k8s/istio/

# Development commands
dev-frontend:
	cd frontend && npm start

dev-user-service:
	cd services/user-service && uvicorn main:app --reload --port 8001

dev-product-service:
	cd services/product-service && uvicorn main:app --reload --port 8002
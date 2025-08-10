# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Taob4o is a Taobao (Chinese e-commerce platform) clone built as a learning project to understand Istio service mesh technology. The project will implement a microservices architecture deployed on Kubernetes with Istio for traffic management, security, and observability.

## Learning Goals

- Istio service mesh concepts and implementation
- Microservices architecture patterns
- Kubernetes deployment and management
- Service-to-service communication and security
- Traffic management and load balancing
- Observability and monitoring in a service mesh

## Planned Architecture

The application will likely include microservices for:
- User authentication and management
- Product catalog
- Shopping cart
- Order processing
- Payment processing
- Inventory management
- Recommendation engine

Each service will be containerized and deployed with Istio sidecar proxies for mesh functionality.

## Current State

- Repository is under MIT License
- Initial commit with basic project structure
- Ready for microservices development and Istio integration

## Project Structure

```
Taob4o/
├── frontend/                 # React frontend with Nginx
│   ├── src/                 # React source code
│   ├── nginx/               # Nginx configuration
│   ├── package.json         # Frontend dependencies
│   └── Dockerfile          # Frontend container build
├── services/                # FastAPI microservices
│   ├── user-service/        # User authentication & management
│   ├── product-service/     # Product catalog
│   ├── cart-service/        # Shopping cart
│   ├── order-service/       # Order processing
│   ├── payment-service/     # Payment handling
│   └── inventory-service/   # Inventory management
├── k8s/                     # Kubernetes configurations
│   ├── deployments/         # Service deployments
│   ├── services/           # Service definitions
│   ├── istio/              # Istio configurations
│   └── configmaps/         # Configuration maps
├── docker-compose.yml       # Local development setup
└── Makefile                # Build and deployment commands
```

## Development Commands

**Local Development (Docker Compose):**
- `make build` - Build all containers
- `make up` - Start all services locally
- `make down` - Stop all services
- `make logs` - View service logs
- `make clean` - Clean up containers and volumes

**Frontend Development:**
- `make dev-frontend` - Start React dev server
- `cd frontend && npm start` - Alternative frontend dev command

**Service Development:**
- `make dev-user-service` - Start user service in dev mode
- `make dev-product-service` - Start product service in dev mode

**Kubernetes Deployment:**
- `make k8s-deploy` - Deploy to Kubernetes
- `make k8s-delete` - Remove from Kubernetes

**Istio Service Mesh:**
- `make istio-install` - Install Istio and enable injection
- `make istio-deploy` - Deploy Istio configurations

## Architecture Notes

- Frontend: React app served via Nginx with API proxy configuration
- Backend: FastAPI microservices with health check endpoints
- Database: PostgreSQL with separate schemas per service
- Service Mesh: Istio for traffic management, security, and observability
- Container Registry: Services use `taobao/service-name:latest` image naming
- Load Balancing: Round-robin for most services, least-connection for user service
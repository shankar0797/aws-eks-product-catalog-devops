# AWS EKS Product Catalog — End-to-End DevOps Project

An end-to-end cloud-native project demonstrating containerization, Infrastructure as Code, Kubernetes deployment, CI/CD automation, container vulnerability scanning, and AWS operations.

## Project Overview

The Product Catalog API is a containerized FastAPI application deployed on Amazon EKS. Infrastructure is provisioned using Terraform, application images are stored in Amazon ECR, and GitHub Actions automates testing, image building, security scanning, and image publishing.

The application is exposed through an AWS Application Load Balancer managed by the AWS Load Balancer Controller.

## Architecture

**Request flow**

Client → Application Load Balancer → Kubernetes Service → Product Catalog Pods

**Delivery flow**

GitHub → GitHub Actions → Automated Tests → Docker Build → Trivy Security Scan → Amazon ECR → EKS Deployment

**Infrastructure**

Terraform provisions the VPC, public and private subnets, routing, NAT Gateway, IAM roles, EKS cluster, managed node group, and ECR repository.

## Technology Stack

- **Cloud:** AWS
- **Infrastructure as Code:** Terraform
- **Containerization:** Docker
- **Container orchestration:** Amazon EKS, Kubernetes
- **Container registry:** Amazon ECR
- **CI/CD:** GitHub Actions
- **Authentication:** GitHub Actions OIDC with AWS IAM
- **Security scanning:** Trivy
- **Application:** Python, FastAPI, Uvicorn
- **Autoscaling:** Kubernetes Horizontal Pod Autoscaler
- **Ingress and load balancing:** AWS Load Balancer Controller and ALB

## Application Endpoints

The deployed API exposes:

| Endpoint | Purpose |
|---|---|
| `/health` | Application health check |
| `/products` | Retrieve the product catalogue |
| `/version` | Return the application version |

The catalogue contains sample Laptop, Keyboard, and Mouse products.

## Implementation Highlights

### Infrastructure as Code
- Provisioned AWS networking and EKS resources using Terraform.
- Used public and private subnets with a NAT Gateway for private-subnet outbound access.
- Defined IAM roles and policies for cluster and worker-node operations.

### Containerization
- Packaged the FastAPI application into a Docker image.
- Configured the application to run as a non-root user.
- Published versioned images to Amazon ECR.

### Kubernetes
- Deployed the application with two replicas.
- Configured readiness and liveness health checks.
- Used a Kubernetes Service and ALB-backed Ingress.
- Configured an HPA with a minimum of two and a maximum of four replicas.

### CI/CD and Security
- Automated Python tests in GitHub Actions.
- Built the Docker image and scanned it using Trivy.
- Configured GitHub OIDC authentication to AWS, avoiding long-lived AWS access keys in GitHub repository secrets.
- Published application images to Amazon ECR.

## Validation Results

During the project validation:

- Both EKS worker nodes reported `Ready`.
- The Product Catalog deployment reported two available replicas.
- Both application pods were running without restarts at the time of evidence capture.
- The `/health` endpoint returned a healthy status.
- The `/products` endpoint returned three sample products.
- The `/version` endpoint returned `1.0.0`.
- The HPA reported CPU utilization and was configured for two to four replicas.
- Terraform validation succeeded, and the plan showed no resources to add or destroy and one proposed EKS tag change.

Command outputs captured during validation are stored in `docs/evidence/`.

## CI/CD Deployment Limitation

The GitHub Actions workflow contains a deployment job for EKS. The test, build, scan, and ECR publishing stages succeeded, but the GitHub-hosted runner timed out when attempting to reach the EKS Kubernetes API.

The EKS public endpoint was restricted to an allowed client IP address, so the GitHub-hosted runner could not connect. The endpoint was not opened to all IP addresses as a workaround.

The application was deployed and validated manually from an authorized client environment. Automated deployment from GitHub-hosted runners therefore remains a network-connectivity limitation in this lab.

A production implementation could use a secured self-hosted runner with controlled network access or another deployment architecture that avoids exposing the Kubernetes API publicly.

## Security Notes

The Trivy workflow checks for HIGH and CRITICAL vulnerabilities and ignores unfixed findings. Passing this configured scan does not mean that the image is free of every vulnerability.

The EKS API is restricted rather than exposed to `0.0.0.0/0`. GitHub Actions authenticates to AWS using OIDC.

This repository intentionally excludes Terraform state, local Terraform variables, credentials, and temporary test artifacts.

## Repository Structure

```text
app/                    FastAPI application
tests/                  Automated tests
terraform/              Terraform infrastructure configuration
k8s/                    Kubernetes manifests and deployment RBAC
.github/workflows/      GitHub Actions workflow
docs/evidence/          Captured validation outputs
Dockerfile              Application container image
.dockerignore           Docker build exclusions
```

## Running Tests Locally

Create and activate a Python virtual environment, then install the development dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

## Cost and Cleanup

This lab uses billable AWS services, including EKS, EC2 worker nodes, NAT Gateway, Elastic IP, ECR storage, and an Application Load Balancer.

Resources should be deleted after testing. Follow `docs/cleanup.md` for the cleanup procedure. Verify that AWS resources created outside Terraform are also removed.

## Project Status

**Implemented and validated:** Terraform infrastructure, containerized API, EKS deployment, ALB access, health checks, HPA configuration, automated testing, container scanning, and ECR publishing.

**Known limitation:** The GitHub-hosted runner cannot reach the restricted EKS API endpoint, so the workflow's automated deployment stage did not complete successfully.

This is a hands-on learning and portfolio project, not a production-certified deployment.
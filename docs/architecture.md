\# AWS EKS Product Catalog — Architecture



\## 1. Overview



This project deploys a containerized FastAPI Product Catalog application on Amazon EKS using Terraform, Docker, Amazon ECR, Kubernetes, and GitHub Actions.



\## 2. Application Request Flow



1\. A client sends an HTTP request to the AWS Application Load Balancer.

2\. The ALB forwards traffic to the Kubernetes Service.

3\. The Service routes traffic to healthy Product Catalog pods.

4\. The application returns the requested product information or health status.



\## 3. CI/CD Flow



1\. Code is pushed to the GitHub repository.

2\. GitHub Actions installs development dependencies and runs automated tests.

3\. The pipeline builds the Docker image.

4\. Trivy scans the image for configured vulnerability severities.

5\. GitHub Actions authenticates to AWS through OIDC.

6\. The image is pushed to Amazon ECR.

7\. The workflow attempts to deploy the image to Amazon EKS.



\*\*Deployment limitation:\*\* The GitHub-hosted runner could not reach the restricted EKS API endpoint. The application was deployed and validated manually from an authorized client environment.



\## 4. Infrastructure



Terraform provisions the core infrastructure:



\- VPC

\- Public and private subnets

\- Internet Gateway

\- Route tables and routes

\- NAT Gateway and Elastic IP

\- IAM roles and policy attachments

\- Amazon EKS cluster and managed node group

\- Amazon ECR repository



Additional components, including the AWS Load Balancer Controller and Kubernetes application resources, are configured separately.



\## 5. Availability and Health



\- Two application replicas

\- Kubernetes readiness and liveness probes

\- HPA configured for a minimum of two and maximum of four replicas

\- ALB health checks using `/health`



\## 6. Security Considerations



\- GitHub Actions uses OIDC for AWS authentication.

\- The EKS API endpoint is restricted to authorized client IPs.

\- The application container runs as a non-root user.

\- Trivy checks HIGH and CRITICAL vulnerabilities while ignoring unfixed findings.

\- Terraform state and local variables must not be committed.



\## 7. Evidence



Validation command outputs are available in `docs/evidence/`.

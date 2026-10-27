\# Part 1: Project Setup and Product Catalog API



\## 1. Objective



Build a working Product Catalog API that will eventually be containerized with Docker and deployed to Amazon EKS using GitHub Actions.



\## 2. Environment



\- Operating system: Windows 11

\- Shell: PowerShell

\- Python: 3.13.1

\- Docker: 29.9.2

\- Git: 2.47.0

\- Application framework: FastAPI

\- Web server: Uvicorn



\## 3. Key Concepts



| Component | Purpose |

|---|---|

| Python | Application programming language |

| Virtual environment | Isolates project dependencies |

| FastAPI | Defines API endpoints and application logic |

| Uvicorn | Runs the application as an HTTP server |

| Docker | Packages the application into a container image |

| Amazon ECR | Stores container images |

| Amazon EKS | Runs and manages Kubernetes workloads |

| GitHub Actions | Automates testing, building, and deployment |



\## 4. Project Commands



\### Navigate to the project



```powershell

cd D:\\downloads\\aws-eks-product-catalog-devops

```



\### Create a virtual environment



```powershell

python -m venv .venv

```



\### Activate the environment



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\### Install dependencies



```powershell

python -m pip install fastapi "uvicorn\[standard]"

```



\### Start the application



```powershell

python -m uvicorn main:app --app-dir app --reload

```



\## 5. API Endpoints



| Endpoint | Expected behavior |

|---|---|

| GET / | Returns application information |

| GET /health | Returns application health status |

| GET /products | Returns all products |

| GET /products/1 | Returns the product with ID 1 |

| GET /version | Returns the application version |



\## 6. Testing Commands



```powershell

Invoke-RestMethod http://localhost:8000/

Invoke-RestMethod http://localhost:8000/health

Invoke-RestMethod http://localhost:8000/products

Invoke-RestMethod http://localhost:8000/products/1

Invoke-RestMethod http://localhost:8000/version

```



All five endpoints returned the expected results during local testing.



\## 7. Important HTTP Status Codes



\- 200 OK: Request completed successfully.

\- 404 Not Found: Requested resource does not exist.

\- 500 Internal Server Error: An unexpected server-side error occurred.



\## 8. Health Checks



The `/health` endpoint currently returns:



```json

{

&#x20; "status": "healthy"

}

```



Kubernetes will later use health probes to determine whether containers are running correctly and ready to receive traffic.



\## 9. Docker Validation



Command:



```powershell

docker run --rm hello-world

```



Result: Successful.



This verified that Docker could pull an image, create a container, execute it, and remove the container after completion.



\## 10. Current Project Status



Completed:



\- Development environment verified.

\- Docker successfully tested.

\- Python virtual environment created.

\- FastAPI and Uvicorn installed.

\- Product Catalog API implemented.

\- Five API endpoints tested successfully.



Pending:



\- Dockerfile and container image.

\- Container security and image optimization.

\- GitHub repository integration.

\- Terraform infrastructure.

\- Amazon ECR and Amazon EKS.

\- GitHub Actions CI/CD.

\- Application Load Balancer.

\- CloudWatch monitoring and alarms.

\- Kubernetes autoscaling, security, rollback, and failure testing.



\## 11. Key Learning



The application currently runs directly on the local machine.



The next stage will package it into a Docker image so that the same application can run consistently in different environments.


\# Part 2: Dockerization Cheat Sheet



\## 1. Project Overview



Application: Product Catalog API  

Framework: FastAPI  

Application server: Uvicorn  

Base image: python:3.13-slim  

Image name: product-catalog:1.0.0  

Container name: product-catalog  

Application port: 8000  

Container user: appuser (UID 10001)



\## 2. Important Files



\- `app/main.py` — FastAPI application code.

\- `app/requirements.txt` — Python application dependencies.

\- `Dockerfile` — Instructions for building the Docker image.

\- `.dockerignore` — Files and directories excluded from the Docker build context.



\## 3. Build and Run Commands



Build an image:



&#x20;   docker build -t product-catalog:1.0.0 .



List images:



&#x20;   docker images



Run a container:



&#x20;   docker run -d --name product-catalog -p 8000:8000 product-catalog:1.0.0



List running containers:



&#x20;   docker ps



List all containers, including stopped ones:



&#x20;   docker ps -a



View logs:



&#x20;   docker logs product-catalog



Follow logs:



&#x20;   docker logs -f product-catalog



Stop a container:



&#x20;   docker stop product-catalog



Start a stopped container:



&#x20;   docker start product-catalog



Remove a stopped container:



&#x20;   docker rm product-catalog



Inspect a container:



&#x20;   docker inspect product-catalog



Check port mapping:



&#x20;   docker port product-catalog



View container resource usage:



&#x20;   docker stats product-catalog



\## 4. Docker Image Inspection



Check which user the image runs as:



&#x20;   docker image inspect --format '{{.Config.User}}' product-catalog:1.0.0



Expected result:



&#x20;   appuser



Check the configured startup command:



&#x20;   docker image inspect --format '{{json .Config.Cmd}}' product-catalog:1.0.0



\## 5. API Validation



Root endpoint:



&#x20;   Invoke-RestMethod http://localhost:8000/



Health endpoint:



&#x20;   Invoke-RestMethod http://localhost:8000/health



List products:



&#x20;   Invoke-RestMethod http://localhost:8000/products



Get product 1:



&#x20;   Invoke-RestMethod http://localhost:8000/products/1



Get application version:



&#x20;   Invoke-RestMethod http://localhost:8000/version



Expected application version: 1.0.0



\## 6. Important Docker Concepts



\### Image

A packaged, read-only template containing the application, dependencies, and required runtime files.



\### Container

A running or stopped instance created from an image.



\### Dockerfile

A file containing instructions for building an image.



\### Build context

The files Docker can access during a build. In this project, `.` specifies the current project directory.



\### Port mapping

`-p 8000:8000` maps host port 8000 to container port 8000.



\### Non-root execution

`USER appuser` runs the application without root privileges inside the container.



\### Docker layer caching

Docker can reuse unchanged build layers. Copying dependency definitions before application source code can reduce rebuild time when only the application code changes.



\### .dockerignore

Excludes unnecessary files from the build context, reducing transfer size and preventing files such as `.venv` and `.env` from being copied into the build context.



\## 7. Troubleshooting Workflow



If the application is unavailable:



1\. Run `docker ps`.

2\. Run `docker ps -a`.

3\. Check `docker logs product-catalog`.

4\. Check `docker port product-catalog`.

5\. Run `docker inspect product-catalog`.

6\. Test the API endpoint again.



If the application code changes:



1\. Rebuild the image with a new tag.

2\. Replace the old container.

3\. Start a container from the new image.

4\. Validate the application endpoints.



\## 8. Security Best Practices



\- Run the application as a non-root user.

\- Use a lightweight base image.

\- Pin direct application dependencies.

\- Exclude local virtual environments and secrets from the build context.

\- Do not store passwords, tokens, or credentials in the Dockerfile.

\- Scan images for known vulnerabilities before production deployment.

\- Keep base images and dependencies updated.

\- Run containers with only the permissions they need.



\## 9. Important Production Considerations



\- A successful image build does not guarantee a healthy application.

\- A successful API test confirms basic functionality, not complete production readiness.

\- `EXPOSE 8000` documents the container port; it does not publish that port on the host.

\- `docker run -p 8000:8000` publishes the port on the host.

\- The current product list is stored in application memory; it is not a persistent database.

\- The `/health` endpoint currently checks basic application responsiveness. It does not validate external dependencies.

\- For production, add automated tests, vulnerability scanning, resource limits, monitoring, and a deployment strategy with health checks.



\## 10. Part 2 Completion Status



\- \[x] Created Dockerfile.

\- \[x] Built the Docker image.

\- \[x] Created a non-root application user.

\- \[x] Started the container.

\- \[x] Tested all five API endpoints.

\- \[x] Practised basic Docker troubleshooting.

\- \[x] Documented Docker commands and concepts.


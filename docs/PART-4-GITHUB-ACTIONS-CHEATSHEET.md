\# Part 4: GitHub Actions CI Cheat Sheet



\## 1. Objective



Learn how to automate application testing using GitHub Actions.



In this project, GitHub Actions:

1\. Detects code changes pushed to GitHub.

2\. Starts a temporary runner.

3\. Checks out the source code.

4\. Configures Python.

5\. Installs dependencies.

6\. Executes automated tests.

7\. Reports success or failure.



\## 2. What Is GitHub Actions?



GitHub Actions is a workflow automation platform integrated with GitHub.



It can automate:

\- Code testing

\- Build processes

\- Code quality checks

\- Docker image builds

\- Container image publishing

\- Application deployments



\## 3. What Is Continuous Integration (CI)?



Continuous Integration means frequently integrating code changes and automatically validating them.



In this project, CI automatically runs tests when code is pushed or a pull request is opened or updated.



\## 4. What Is Continuous Delivery/Deployment (CD)?



Continuous Delivery prepares validated changes for release.



Continuous Deployment automatically deploys validated changes to the target environment.



Our current workflow implements CI testing. It does not yet deploy the application to AWS.



\## 5. Project Structure



```text

aws-eks-product-catalog-devops/

├── .github/

│   └── workflows/

│       └── ci.yml

├── app/

├── tests/

├── Dockerfile

└── requirements-dev.txt

```



GitHub Actions workflow files must be stored under:



```text

.github/workflows/

```



\## 6. Workflow File



File: `.github/workflows/ci.yml`



```yaml

name: Product Catalog CI



on:

&#x20; push:

&#x20; pull\_request:



permissions:

&#x20; contents: read



jobs:

&#x20; test:

&#x20;   name: Run Python Tests

&#x20;   runs-on: ubuntu-latest



&#x20;   steps:

&#x20;     - name: Checkout source code

&#x20;       uses: actions/checkout@v6



&#x20;     - name: Set up Python

&#x20;       uses: actions/setup-python@v6

&#x20;       with:

&#x20;         python-version: "3.13"



&#x20;     - name: Install dependencies

&#x20;       run: python -m pip install -r requirements-dev.txt



&#x20;     - name: Run automated tests

&#x20;       run: python -m pytest -v

```



\## 7. Understand Each YAML Section



\### `name`



```yaml

name: Product Catalog CI

```



Sets the workflow name displayed in GitHub Actions.



\### `on`



```yaml

on:

&#x20; push:

&#x20; pull\_request:

```



Defines the events that trigger the workflow.



\- `push`: Runs when commits are pushed.

\- `pull\_request`: Runs for applicable pull request events.



\### `permissions`



```yaml

permissions:

&#x20; contents: read

```



Grants the workflow read access to repository contents.



Use the minimum permissions required by each workflow.



\### `jobs`



```yaml

jobs:

&#x20; test:

```



Defines a job with the identifier `test`.



\### `runs-on`



```yaml

runs-on: ubuntu-latest

```



Requests a GitHub-hosted Ubuntu runner. The job executes on that runner.



\### `steps`



Steps define the individual operations performed by the job.



\### `uses`



```yaml

uses: actions/checkout@v6

```



Uses a reusable GitHub Action to check out the repository.



\### `with`



```yaml

with:

&#x20; python-version: "3.13"

```



Passes configuration to the action. Here, it selects Python 3.13.



\### `run`



```yaml

run: python -m pytest -v

```



Executes a shell command on the runner.



\## 8. What Happens During a Workflow Run?



\### Step 1: Trigger



You push a commit:



```powershell

git push

```



GitHub detects the push event.



\### Step 2: Runner starts



GitHub provisions a hosted Ubuntu runner for the job.



\### Step 3: Checkout



The checkout action retrieves the repository source code.



\### Step 4: Python setup



The setup action configures Python 3.13.



\### Step 5: Dependency installation



```powershell

python -m pip install -r requirements-dev.txt

```



Installs the dependencies required for testing.



\### Step 6: Automated testing



```powershell

python -m pytest -v

```



Runs the automated tests.



\### Step 7: Result



\- Green check: The workflow succeeded.

\- Red cross: At least one required step failed.



\## 9. Important Git Commands



Check repository status:



```powershell

git status

```



Stage changes:



```powershell

git add .

```



Stage one file:



```powershell

git add requirements-dev.txt

```



Commit changes:



```powershell

git commit -m "Describe the change"

```



Push commits:



```powershell

git push

```



View recent commits:



```powershell

git log --oneline -5

```



Check configured remotes:



```powershell

git remote -v

```



\## 10. Typical Development Workflow



```text

Modify code

&#x20;   |

&#x20;   v

Run tests locally

&#x20;   |

&#x20;   v

git add

&#x20;   |

&#x20;   v

git commit

&#x20;   |

&#x20;   v

git push

&#x20;   |

&#x20;   v

GitHub Actions starts

&#x20;   |

&#x20;   v

Install dependencies

&#x20;   |

&#x20;   v

Run automated tests

&#x20;   |

&#x20;   v

Review success or failure

```



\## 11. Troubleshooting



\### Workflow does not appear



Check:

\- Workflow file is under `.github/workflows/`.

\- File has a `.yml` or `.yaml` extension.

\- The workflow has been committed and pushed.

\- The triggering event matches the workflow configuration.



\### Dependency installation fails



Inspect the Install dependencies step.



Check:

\- `requirements-dev.txt` exists in the repository root.

\- All referenced requirement files exist.

\- Package names and versions are valid.

\- Package versions are compatible.



\### Tests fail during collection



Inspect the Run automated tests step.



Check:

\- Python imports

\- Test file names

\- Installed dependencies

\- Application imports

\- TestClient compatibility



\### Tests pass locally but fail in CI



Remember that the runner is a separate environment.



Check Python versions, dependency versions, environment variables, and platform-specific behavior.



\### YAML configuration error



Check:

\- Indentation

\- Colons and list markers

\- Correct workflow file path

\- Correct action references



YAML indentation is significant.



\## 12. Security Best Practices



\- Give workflows only the permissions they need.

\- Do not hardcode AWS credentials in YAML.

\- Store necessary credentials in GitHub Secrets or use OIDC where appropriate.

\- Prefer short-lived AWS credentials through GitHub OIDC for AWS deployments.

\- Review third-party actions before using them.

\- Pin third-party actions to verified commit SHAs when stronger supply-chain security is required.

\- Do not print secrets in workflow logs.



\## 13. Interview Questions



\### Q1. What is GitHub Actions?



GitHub Actions automates workflows such as testing, building, and deploying applications in response to repository events.



\### Q2. What is a workflow?



A workflow is an automated process defined in a YAML file under `.github/workflows/`.



\### Q3. What is a runner?



A runner is the machine that executes a workflow job.



\### Q4. What is the difference between a job and a step?



A job is a group of steps executed on a runner. A step is an individual action or command within that job.



\### Q5. What is the difference between CI and CD?



CI validates code changes automatically. CD automates preparing releases or deploying validated changes.



\### Q6. How do you troubleshoot a failed workflow?



Open the failed run, inspect the first failed step, read its logs, reproduce the issue locally if possible, fix the problem, test it, and push a new commit.



\### Q7. Why do tests pass locally but fail in CI?



The environments may differ in dependencies, Python versions, configuration, environment variables, or operating-system behavior.



\### Q8. Does our current workflow deploy to AWS?



No. It performs continuous integration by installing dependencies and running automated tests. AWS image publishing and deployment will be added in later stages.



\## 14. Current Project Status



Completed:

\- FastAPI application

\- Docker image and container

\- Automated tests

\- Git repository and GitHub remote

\- GitHub Actions CI workflow

\- Dependency issue fixed

\- Successful CI run



Next:

\- Improve Docker image security and efficiency

\- Publish the image to Amazon ECR

\- Provision AWS infrastructure with Terraform

\- Deploy to Amazon EKS

\- Extend the pipeline with controlled deployment



\## 15. Key Takeaway



GitHub Actions automates validation of code changes.



Our current workflow checks out the source code, configures Python, installs dependencies, and executes Pytest. A successful run confirms that the configured checks passed in the CI environment.




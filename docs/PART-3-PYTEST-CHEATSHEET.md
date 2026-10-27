\# Part 3: Python Automated Testing with Pytest



\## 1. Objective



Learn how to test a Python FastAPI application automatically using Pytest.



In this project, we test the Product Catalog API before deploying it.



\## 2. What Is Automated Testing?



Automated testing uses code to verify whether an application behaves as expected.



Instead of manually checking every API endpoint, we write tests that check:

\- HTTP status codes

\- API response data

\- Successful requests

\- Error responses

\- Application behavior after code changes



Benefits:

\- Detect bugs early

\- Reduce manual testing

\- Prevent regressions

\- Integrate testing into CI/CD pipelines



\## 3. What Is Pytest?



Pytest is a Python testing framework.



It discovers test files, executes test functions, evaluates assertions, and reports failures.



Install Pytest:



```powershell

python -m pip install pytest

```



Check the installed version:



```powershell

python -m pytest --version

```



\## 4. Project Structure



```text

aws-eks-product-catalog-devops/

├── app/

│   ├── main.py

│   └── requirements.txt

├── tests/

│   └── test\_main.py

├── requirements-dev.txt

└── Dockerfile

```



`app/main.py` contains the application.



`tests/test\_main.py` contains automated tests.



`requirements-dev.txt` contains application dependencies and additional testing dependencies.



\## 5. Development Dependencies



Example `requirements-dev.txt`:



```text

\-r app/requirements.txt

pytest==9.1.1

httpx2

```



Explanation:



\- `-r app/requirements.txt`: Install the application's dependencies.

\- `pytest==9.1.1`: Install the specified Pytest version.

\- `httpx2`: Provides the dependency required by the current Starlette TestClient version in this environment.



Install the development dependencies:



```powershell

python -m pip install -r requirements-dev.txt

```



Note: Keep dependency versions compatible with your FastAPI and Starlette versions. For reproducible builds, pin and test dependency versions.



\## 6. Understanding the Test File



File: `tests/test\_main.py`



Example:



```python

from fastapi.testclient import TestClient



from app.main import app



client = TestClient(app)





def test\_health\_endpoint():

&#x20;   response = client.get("/health")



&#x20;   assert response.status\_code == 200

&#x20;   assert response.json() == {"status": "healthy"}

```



Explanation:



\- `TestClient`: Sends requests to the application without starting a separate server.

\- `app`: Imports the FastAPI application.

\- `client.get("/health")`: Sends a GET request to the health endpoint.

\- `response.status\_code`: Checks the HTTP status code.

\- `response.json()`: Reads the JSON response.

\- `assert`: Verifies that a condition is true.



If an assertion fails, Pytest reports the test as failed.



\## 7. Important Pytest Naming Rules



Pytest automatically discovers files commonly named:



```text

test\_\*.py

\*\_test.py

```



Test functions should generally start with:



```python

def test\_example():

&#x20;   ...

```



Example:



```python

def test\_addition():

&#x20;   assert 2 + 3 == 5

```



\## 8. Run Tests



Run all tests with detailed output:



```powershell

python -m pytest -v

```



Run tests from a specific directory:



```powershell

python -m pytest tests/

```



Run one test file:



```powershell

python -m pytest tests/test\_main.py -v

```



Run one test function:



```powershell

python -m pytest tests/test\_main.py::test\_health\_endpoint -v

```



Stop after the first failure:



```powershell

python -m pytest -x

```



Show additional output:



```powershell

python -m pytest -vv

```



\## 9. Tests in This Project



The Product Catalog API currently has six tests:



| Test | Expected result |

|---|---|

| Root endpoint | HTTP 200 and expected message |

| Health endpoint | HTTP 200 and healthy status |

| List products | HTTP 200 and three products |

| Existing product | HTTP 200 and product details |

| Nonexistent product | HTTP 404 |

| Version endpoint | HTTP 200 and version 1.0.0 |



Expected summary:



```text

6 passed

```



\## 10. Important HTTP Status Codes



| Status code | Meaning |

|---|---|

| 200 | Request succeeded |

| 201 | Resource created |

| 400 | Bad request |

| 401 | Authentication required or invalid |

| 403 | Access forbidden |

| 404 | Resource not found |

| 500 | Internal server error |

| 503 | Service unavailable |



\## 11. Local Testing vs. CI Testing



Local testing:



```powershell

python -m pytest -v

```



CI testing:



```yaml

\- name: Run automated tests

&#x20; run: python -m pytest -v

```



Local testing uses your computer's Python environment.



GitHub Actions runs the tests on a separate runner with its own Python environment.



The CI environment must install all required dependencies independently.



\## 12. Common Problems



\### Problem: No tests collected



Check:

\- Test file name

\- Test function names

\- Correct project directory

\- Test file location



\### Problem: ModuleNotFoundError



Possible causes:

\- Missing package

\- Incorrect import

\- Dependencies not installed

\- Incorrect working directory



\### Problem: TestClient dependency error



Check the installed FastAPI and Starlette versions.



Install compatible dependencies through your requirements files instead of relying on packages installed manually in your local environment.



\### Problem: Tests pass locally but fail in CI



Check:

\- Python version

\- Dependency versions

\- Environment variables

\- File paths and capitalization

\- CI installation logs



\## 13. Best Practices



\- Write tests for successful and unsuccessful requests.

\- Keep tests independent.

\- Use meaningful test names.

\- Test expected behavior, not implementation details.

\- Run tests before committing code.

\- Add tests for every bug fixed.

\- Keep development dependencies separate from runtime dependencies.

\- Never commit credentials or secrets.

\- Run tests automatically in CI.



\## 14. Interview Questions



\### Q1. What is Pytest?



Pytest is a Python testing framework that discovers and executes tests and reports whether assertions pass or fail.



\### Q2. Why do we use automated testing?



Automated testing helps identify bugs early, prevents regressions, and reduces repetitive manual testing.



\### Q3. What is an assertion?



An assertion checks whether an expected condition is true. Pytest marks the test as failed if the assertion is false.



\### Q4. How do you run tests?



```powershell

python -m pytest -v

```



\### Q5. What is TestClient?



FastAPI's TestClient allows us to test application endpoints without running a separate HTTP server.



\### Q6. Why can tests pass locally but fail in GitHub Actions?



The environments may differ in dependencies, Python versions, configuration, environment variables, or filesystem behavior.



\## 15. Key Takeaway



Pytest verifies that the application behaves correctly.



GitHub Actions can run the same tests automatically whenever code is pushed or a pull request is created.




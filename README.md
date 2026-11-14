# DevOps Journey API

A small Python API to use as the application for an end-to-end DevOps project. It includes a health endpoint and a versioned item API. Containerization, Kubernetes, Helm, GitHub Actions, and Argo CD are intentionally left for the DevOps implementation phase.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Welcome message and useful links |
| `GET` | `/health` | Health check |
| `GET` | `/api/v1/items` | List sample items |
| `GET` | `/api/v1/items/{item_id}` | Get an item by ID; returns `404` when missing |

## Run tests

```powershell
python -m pytest
```

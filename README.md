# DevOps Journey

A beginner-friendly learning hub that explains how code moves from a developer's laptop to production. Each module introduces **what** a tool does, **why** teams use it, a practical **first step**, and links to official documentation or recognized DevOps research.

The learning path covers Git and collaboration, CI/CD with GitHub Actions, Docker and multi-stage builds, Kubernetes, cluster planning and Terraform, Helm, GitOps with Argo CD, ingress and traffic routing, DNS, observability with Prometheus, security, and an end-to-end delivery walkthrough.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` for the learning hub. Use the search field or topic filters to explore modules, and mark modules complete to track progress in your browser.

## API and docs

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | DevOps learning hub |
| `GET` | `/health` | Health check |
| `GET` | `/api/v1/items` | List sample API items |
| `GET` | `/api/v1/items/{item_id}` | Get an item by ID; returns `404` when missing |
| `GET` | `/docs` | Interactive OpenAPI documentation |

## Run tests

```powershell
python -m pytest
```

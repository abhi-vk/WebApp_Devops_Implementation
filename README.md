# DevOps Journey

A practical learning hub for understanding how code moves from development to production. Explore concise explanations of DevOps tools and practices, with hands-on starting points and links to official resources.

## Topics

Git, CI/CD, GitHub Actions, Docker, Kubernetes, Terraform, Helm, Argo CD, ingress, DNS, observability, security, and end-to-end delivery.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Search and filter learning modules, or mark topics complete to track progress in your browser.

## Test

```powershell
python -m pytest
```

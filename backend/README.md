VisionBharatSphere - Backend (FastAPI)

Quick start (local, virtualenv)

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the API locally:

```bash
uvicorn app.main:app --reload --port 8000
```

Docker (recommended for reproducible dev and deploy)

Build and run using docker-compose (uses SQLite by default):

```bash
# build and run
docker compose up --build

# stop
docker compose down
```

To use Postgres locally with docker-compose, uncomment the `postgres` service in `docker-compose.yml` and set `DATABASE_URL=postgresql://vbs:vbs_pass@postgres:5432/vbs` in your environment before starting.

Endpoints
- POST /auth/register -> register {email, full_name, password}
- POST /auth/login -> login {email, password} returns bearer token
- GET /products -> list products
- POST /products -> create product (no auth in this simple demo)
- POST /tests -> submit test (requires Authorization: Bearer <token>)

Production notes & deploying with Vercel

- Vercel is ideal for hosting the frontend (Next.js). The Python FastAPI backend is best hosted on a dedicated server or platform (Render, Railway, Fly, Google Cloud Run, AWS ECS, etc.) or container registry. Use the provided `Dockerfile` to package the backend for such platforms.
- Use environment variables for secrets and DB connections: `VBS_SECRET`, `DATABASE_URL` (Postgres), and any other production configs. Do NOT commit secrets to the repository.
- Recommended production stack:
	- Frontend: Next.js on Vercel (uses client-side calls to backend API)
	- Backend: containerized FastAPI (Docker) on Render/Railway/Fly/Cloud Run
	- Database: managed Postgres (db URL in `DATABASE_URL`)

ERP / Optometrist features (next steps)
- Add role-based users (patient, optometrist, admin)
- Add product catalog, inventory, orders, and appointment scheduling
- Add admin dashboard for optometrists to view patient tests and orders

If you want, I can:
- Add Dockerfile + docker-compose (done)
- Add a small Docker-based local demo 'deploy' script
- Move the Ishihara page into the Next.js frontend and implement secure auth flow (HttpOnly cookie or token-based)

*** End README

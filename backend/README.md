# EcoSphere Backend

FastAPI + SQLModel + MySQL backend for the **EcoSphere ESG Management Platform** — measuring Environmental, Social, and Governance performance with gamification, scoring, and reporting.

## Tech Stack

- **FastAPI** — REST API with auto-generated Swagger docs
- **SQLModel** — ORM + Pydantic schemas in one (SQLAlchemy underneath)
- **MySQL** via **PyMySQL**
- **JWT** auth (`python-jose`) + **bcrypt** password hashing (`passlib`)

## Quick Start

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # then edit DATABASE_URL and JWT_SECRET
```

Create the MySQL database:

```sql
CREATE DATABASE ecosphere_db;
CREATE USER 'ecosphere_user'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON ecosphere_db.* TO 'ecosphere_user'@'localhost';
FLUSH PRIVILEGES;
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Seed demo data:

```bash
python seed.py
```

- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Demo Accounts (after seed)

| Email | Password | Role |
|---|---|---|
| admin@ecosphere.com | admin123 | Admin |
| employee@ecosphere.com | employee123 | Employee |

## Architecture

```
routers/  → thin HTTP layer (parse request, call service, return response)
services/ → all business logic + DB queries (no separate repository layer for MVP)
models/   → SQLModel table=True classes — this IS the MySQL schema
schemas/  → request/response shapes that differ from DB models (auth, approvals, etc.)
```

**Deliberate MVP choices:**

- **No Alembic** — tables are created on startup via `SQLModel.metadata.create_all()`. Add Alembic before production.
- **Sync SQLAlchemy** — simpler for a one-day build; async drivers add setup risk with little payoff at hackathon scale.
- **Cross-cutting modules** — `notifications/` and `reports/` are separate from feature routers because they are called from multiple services.

## API Prefix

All endpoints are mounted under `/api` to match the frontend (`frontend/src/api/endpoints.js`).

## Project Structure

See the build guide in the repo root for the full folder map. Key modules:

| Module | Routes |
|---|---|
| Auth | `/api/auth/register`, `/api/auth/login` |
| Departments | `/api/departments`, `/api/departments/{id}/score` |
| Environmental | `/api/emission-factors`, `/api/carbon-transactions`, `/api/goals` |
| Social | `/api/csr-activities`, `/api/participations/{id}/approve` |
| Gamification | `/api/challenges`, `/api/rewards/{id}/redeem`, `/api/leaderboard` |
| Governance | `/api/policies`, `/api/compliance-issues`, `/api/audits` |
| Scoring | `/api/organization/score`, `/api/dashboard/summary` |
| Settings | `/api/settings/esg`, `/api/settings/notifications` |

## Shared Enums

`app/constants/enums.py` is the single source of truth for status values shared with the frontend (`frontend/src/constants/enums.js`). Keep them in sync.

## Environment Variables

See `.env.example` for all required keys.

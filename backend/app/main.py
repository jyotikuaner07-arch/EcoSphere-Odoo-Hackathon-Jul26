from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.database import init_db
from app.middleware.error_handler import register_exception_handlers
from app.routers import (
    audit_router,
    auth_router,
    badge_router,
    carbon_transaction_router,
    category_router,
    challenge_participation_router,
    challenge_router,
    compliance_issue_router,
    csr_activity_router,
    dashboard_router,
    department_router,
    employee_router,
    emission_factor_router,
    goal_router,
    notification_router,
    participation_router,
    policy_router,
    report_router,
    reward_router,
    scoring_router,
    settings_router,
)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    lifespan=lifespan,
)

origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

upload_path = Path(settings.UPLOAD_DIR)
upload_path.mkdir(parents=True, exist_ok=True)
app.mount(f"/{settings.UPLOAD_DIR}", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

API_PREFIX = "/api"

app.include_router(auth_router.router, prefix=API_PREFIX)
app.include_router(department_router.router, prefix=API_PREFIX)
app.include_router(category_router.router, prefix=API_PREFIX)
app.include_router(emission_factor_router.router, prefix=API_PREFIX)
app.include_router(carbon_transaction_router.router, prefix=API_PREFIX)
app.include_router(goal_router.router, prefix=API_PREFIX)
app.include_router(csr_activity_router.router, prefix=API_PREFIX)
app.include_router(participation_router.router, prefix=API_PREFIX)
app.include_router(challenge_router.router, prefix=API_PREFIX)
app.include_router(challenge_participation_router.router, prefix=API_PREFIX)
app.include_router(badge_router.router, prefix=API_PREFIX)
app.include_router(employee_router.router, prefix=API_PREFIX)
app.include_router(reward_router.router, prefix=API_PREFIX)
app.include_router(policy_router.router, prefix=API_PREFIX)
app.include_router(audit_router.router, prefix=API_PREFIX)
app.include_router(compliance_issue_router.router, prefix=API_PREFIX)
app.include_router(scoring_router.router, prefix=API_PREFIX)
app.include_router(dashboard_router.router, prefix=API_PREFIX)
app.include_router(dashboard_router.router_leaderboard, prefix=API_PREFIX)
app.include_router(notification_router.router, prefix=API_PREFIX)
app.include_router(report_router.router, prefix=API_PREFIX)
app.include_router(settings_router.router, prefix=API_PREFIX)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.PROJECT_NAME}

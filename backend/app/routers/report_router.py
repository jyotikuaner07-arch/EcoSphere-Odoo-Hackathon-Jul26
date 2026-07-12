from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.database import get_session
from app.reports.service import build_report_summary

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/{report_type}")
def get_report(
    report_type: str,
    department_id: Optional[int] = Query(default=None),
    session: Session = Depends(get_session),
):
    summary = build_report_summary(session, department_id)
    return {"type": report_type, **summary}


@router.post("/custom")
def custom_report(
    filters: dict,
    session: Session = Depends(get_session),
):
    department_id = filters.get("department_id")
    return build_report_summary(session, department_id)


@router.get("/{report_id}/export")
def export_report(report_id: str, format: str = Query(default="csv")):
    return {
        "report_id": report_id,
        "format": format,
        "message": "Export stub — integrate PDF/Excel/CSV generator as needed.",
    }

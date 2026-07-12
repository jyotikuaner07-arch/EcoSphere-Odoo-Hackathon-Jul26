import os
import uuid
from pathlib import Path

from fastapi import UploadFile

from app.config import settings


def save_upload_file(upload: UploadFile, subfolder: str = "proofs") -> str:
    """Save an uploaded file and return its relative URL path."""
    upload_dir = Path(settings.UPLOAD_DIR) / subfolder
    upload_dir.mkdir(parents=True, exist_ok=True)

    ext = Path(upload.filename or "file").suffix
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = upload_dir / filename

    with open(filepath, "wb") as f:
        f.write(upload.file.read())

    return f"/{settings.UPLOAD_DIR}/{subfolder}/{filename}".replace("\\", "/")

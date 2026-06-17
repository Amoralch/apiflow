import os
import uuid

from fastapi import APIRouter, Request, UploadFile, File, HTTPException

router = APIRouter()

ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".gif", ".mp4", ".webp"}
MAX_SIZE = 25 * 1024 * 1024


@router.post("/upload")
async def upload(request: Request, file: UploadFile = File(...)):
      settings = request.app.state.db  # access via app state
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_EXT:
              raise HTTPException(400, f"File type {e

from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

router = APIRouter()


class EngagementData(BaseModel):
      likes: int = 0
      shares: int = 0
      comments: int = 0
      impressions: int = 0


@router.get("/weekly")
async def weekly(request: Request):
      db = request.app.state.db
      summary = await db.weekly_summary()
      return summary


@router.get("/post/{post_id}")
async def post_engagement(request: Request, post_id: int):
      db = request.app.state.db
  

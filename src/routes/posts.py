from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

router = APIRouter()


class CreatePost(BaseModel):
      title: str
      body: str = ""
      platform: str = "general"
      scheduled_at: str | None = None
      media_ids: list[int] | None = None


class UpdateStatus(BaseModel):
      status: str


@router.post("/")
async def create(request: Request, data: CreatePost):
      db = request.app.state.db
      post_id = await db.create_post(
          title=data.title,
          

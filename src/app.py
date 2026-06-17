import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

from src.config import get_settings
from src.database import Database
from src.scheduler import PostScheduler
from src.routes import posts, media, analytics, auth


@asynccontextmanager
async def lifespan(app: FastAPI):
      settings = get_settin

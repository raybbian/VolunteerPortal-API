import asyncio

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from website.api.auth import auth
from website.api.data import data
from website.api.admin import admin
from website.api.training import training
from website.api.views import views
from website.api.school import school
from website.api.program import program
from website.core.database import init_database

app = FastAPI()

app.mount("/static", StaticFiles(directory="website/static"), name="static")
app.include_router(auth, tags=["auth"])
app.include_router(admin, tags=["admin"])
app.include_router(school, tags=["school"])
app.include_router(program, tags=["program"])
app.include_router(data, tags=["data"])
app.include_router(training, tags=["training"])
app.include_router(views, tags=["views"])

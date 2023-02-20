from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.middleware.db_middleware import init_session_instance
from app.routes import register_routes

app = FastAPI()

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.add_middleware(BaseHTTPMiddleware, dispatch=init_session_instance)

register_routes(app)

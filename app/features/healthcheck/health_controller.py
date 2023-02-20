import datetime

from fastapi import APIRouter, Response, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.features.healthcheck.health_schemas import HealthCheck, StatusHealth
from app.infrastructure.db.database import get_db

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("", response_model=HealthCheck, name="HealthCheck")
def get_health_status(response: Response):
    data = HealthCheck(tag=settings.app_version, app_name=settings.app_name)
    data.entities.update({"database": status_text(is_database_online())})

    data.time = str(datetime.datetime.now())
    data.status = StatusHealth.HEALTHY

    if any(list(filter(lambda v: v[1] != StatusHealth.HEALTHY, data.entities.items()))):
        data.status = StatusHealth.UNHEALTHY
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return data


def status_text(status: bool):
    return StatusHealth.HEALTHY if status else StatusHealth.UNHEALTHY


def is_database_online():
    try:
        session = get_db()
        session.execute(text("SELECT 1"))
    except (SQLAlchemyError, TimeoutError):
        return False
    return True

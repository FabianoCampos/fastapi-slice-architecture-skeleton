from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str | None
    tag: str | None
    app_name: str | None
    time: str | None
    entities: dict[str, str] | None = {}


class StatusHealth:
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"

import logging

from app.core.config import settings

logging.basicConfig(
    level=logging.getLevelName(settings.logging_level.upper()),
    format="%(levelname)s: [%(asctime)s] - %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger()

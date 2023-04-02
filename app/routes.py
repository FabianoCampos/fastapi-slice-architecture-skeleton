import importlib
from pathlib import Path

from fastapi import FastAPI


def register_routes(app: FastAPI) -> None:
    features_dir = Path.cwd() / "app" / "features"
    for entry in features_dir.glob("**/*_controller.py"):
        module_name = f"app.features.{entry.parent.name}.{entry.stem}"
        try:
            module = importlib.import_module(module_name)
            app.include_router(module.router)
        except ImportError as e:
            print(f"Falha o importar {module_name}: {e}")

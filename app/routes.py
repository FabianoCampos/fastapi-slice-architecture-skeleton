import os

from fastapi import FastAPI


def register_routes(app: FastAPI) -> None:
    features = os.path.join(os.getcwd(), "app", "features")
    for entry in scanfiles(features):
        if entry.name.endswith("_controller.py"):
            file_import = f"{entry.name}"[:-3]
            feature_module = (
                entry.path.replace(features + os.sep, "")
                .replace(os.sep + entry.name, "")
                .replace(os.sep, ".")
            )
            str_importer = f"from app.features.{feature_module} import {file_import}"
            str_register = f"app.include_router({file_import}.router)"
            exec(str_importer)
            exec(str_register)


def scanfiles(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield from scanfiles(entry)
        else:
            yield entry

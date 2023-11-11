import uuid

from django.db.models import Model
from django.utils.text import slugify


def get_image_upload_path(instance: type[Model], filename: str) -> str:
    extension = filename.split(".")[-1]
    try:
        path, name = instance.image_upload_path_and_name
        name = slugify(name)
    except (AttributeError, ValueError):
        path = "images/upload/"
        name = uuid.uuid4().hex
    return f"{path}{name}.{extension.lower()}"

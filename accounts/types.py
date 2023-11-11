import strawberry
from strawberry import auto

from . import models


@strawberry.django.type(models.User)
class User:
    id: auto  # noqa: A003
    username: auto
    first_name: auto
    last_name: auto

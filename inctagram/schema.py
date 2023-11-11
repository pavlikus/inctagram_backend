import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension

from accounts.types import User


@strawberry.type
class Query:
    users: list[User] = strawberry.django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)

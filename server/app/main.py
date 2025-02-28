import strawberry
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class Query:
    @strawberry.field(description="Hello world")
    async def hello(self) -> str:
        return "Hello, World!"

schema = strawberry.Schema(query=Query)

app = web.Application()

app.router.add_route("*", "/graphql", GraphQLView(schema=schema))


if __name__ == "__main__":
    web.run_app(app)

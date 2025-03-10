import strawberry
from strawberry.aiohttp.views import GraphQLView
from aiohttp import web

from app.graphql.graphql_query import Query


# @strawberry.type
# class Mutation:
#     ...

schema = strawberry.Schema(query=Query)

app = web.Application()
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))


if __name__ == "__main__":
    web.run_app(app, port=8000)

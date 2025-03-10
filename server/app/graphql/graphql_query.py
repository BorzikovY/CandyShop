import strawberry

from app.graphql.graphql_schemas import Candy, Category
from app.test_data import candies, categories


@strawberry.type
class Query:
    @strawberry.field
    async def candies(
        self,
        category_id: int | None = None,
        search: str | None = None,
        in_stock: bool | None = None
    ) -> list[Candy]:
        filtered = candies
        if category_id:
            filtered = [c for c in filtered if c.category_id == category_id]
        if search:
            search_lower = search.lower()
            filtered = [c for c in filtered if search_lower in c.name.lower()]
        if in_stock is not None:
            filtered = [c for c in filtered if c.in_stock == in_stock]
        return filtered

    @strawberry.field
    async def candy(self, id: int) -> Candy | None:
        return next((c for c in candies if c.id == id), None)

    @strawberry.field
    async def categories(self) -> list[Category]:
        return categories

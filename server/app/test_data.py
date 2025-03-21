from app.graphql.graphql_schemas import Candy, Category


categories = [
    Category(id=1, name="Шоколадные", description="Конфеты с шоколадом"),
    Category(id=2, name="Жевательные", description="Мармелад и жевательные конфеты"),
    Category(id=3, name="Леденцы", description="Твердые карамельные конфеты"),
]

candies = [
    Candy(
        id=1,
        name="Шоколадный мишка",
        price=2.99,
        category_id=1,
        description="Милый мишка из молочного шоколада",
        in_stock=True
    ),
    Candy(
        id=2,
        name="Фруктовый мармелад",
        price=1.99,
        category_id=2,
        description="Ассорти фруктовых вкусов",
        in_stock=True
    ),
    Candy(
        id=3,
        name="Мятный леденец",
        price=0.99,
        category_id=3,
        description="Освежающий мятный вкус",
        in_stock=False
    ),
]

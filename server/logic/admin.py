from django.contrib import admin
from logic.models import (
    Candy,
    Order,
    OrderedCandy
)


admin.site.register(Candy)
admin.site.register(Order)
admin.site.register(OrderedCandy)

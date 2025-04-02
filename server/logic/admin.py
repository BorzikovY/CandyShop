from django.contrib import admin
from logic.models import (
    Candy,
    Order,
    OrderedCandy,
    Feedback
)


admin.site.register(Candy)
admin.site.register(Order)
admin.site.register(OrderedCandy)
admin.site.register(Feedback)

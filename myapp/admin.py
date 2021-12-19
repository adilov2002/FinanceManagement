from django.contrib import admin
from .models import Categories, Items, Purchases, Feedback, Income


admin.site.register(Categories)
admin.site.register(Items)
admin.site.register(Purchases)
admin.site.register(Feedback)
admin.site.register(Income)


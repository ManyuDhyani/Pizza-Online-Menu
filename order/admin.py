from django.contrib import admin

from .models import (
    Category, Topping, Pizza, Prize, Size,
    Prizesize, About, Contact
)

admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Prize)
admin.site.register(Size)
admin.site.register(Pizza)
admin.site.register(Prizesize)
admin.site.register(About)
admin.site.register(Contact)
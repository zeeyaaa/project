from django.contrib import admin
from .models import Chocolate


class ChocolateAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quantity')

admin.site.register(Chocolate, ChocolateAdmin)

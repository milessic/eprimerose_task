from django.contrib import admin
from .models import Currencies



class CurrenciesAdmin(admin.ModelAdmin):
    search_fields = ('currency_pair',)
    list_display = [field.name for field in Currencies._meta.get_fields()]
    list_filter = ["base_currency", "quote_currency"]

# Register your models here.
admin.site.register(Currencies, CurrenciesAdmin)

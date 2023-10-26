from django.contrib import admin
from .models import Currencies
from rangefilter.filters import DateRangeFilterBuilder


class CurrenciesAdmin(admin.ModelAdmin):
    # basic admin interface with search field for currency_pair field, list display for all fields
    #   and filters for utc_timestamp (3rd party app django-rangefilter, built in filters for base_currency and quote_currency
    search_fields = ('currency_pair',)
    list_display = [field.name for field in Currencies._meta.get_fields()]
    list_filter = [("utc_timestamp", DateRangeFilterBuilder()), "base_currency", "quote_currency"]

# Register your models here.
admin.site.register(Currencies, CurrenciesAdmin)

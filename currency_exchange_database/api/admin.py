from django.contrib import admin
from .models import CurrencyRates, Currencies
from rangefilter.filters import DateRangeFilterBuilder


class CurrenciesAdmin(admin.ModelAdmin):
    search_fields = ('currency_code',)
    list_display = ('currency_code', )


class CurrencyRatesAdmin(admin.ModelAdmin):
    # basic admin interface with search field for currency_pair field, list display for all fields
    #   and filters for utc_timestamp (3rd party app django-rangefilter, built in filters for base_currency and quote_currency
    #   search fields searches for currency_code attirbute of base_currency or quote_currency
    search_fields = ('base_currency__currency_code', 'quote_currency__currency_code')
    list_display = [field.name for field in CurrencyRates._meta.get_fields()]
    list_filter = [("utc_timestamp", DateRangeFilterBuilder()), "base_currency", "quote_currency"]


# Register your models here.
admin.site.register(CurrencyRates, CurrencyRatesAdmin)
admin.site.register(Currencies, CurrenciesAdmin)

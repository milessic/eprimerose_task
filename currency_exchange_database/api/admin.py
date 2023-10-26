from django.contrib import admin
from .models import Currencies


class CurrenciesAdmin(admin.ModelAdmin):
    search_fields = ('open_rate')
    list_display = [field.name for field in Currencies._meta.get_fields()]


# Register your models here.
admin.site.register(Currencies)

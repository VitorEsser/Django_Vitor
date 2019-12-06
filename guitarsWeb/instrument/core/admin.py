from django.contrib import admin
from .models import Instrument, Brand

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_brands', 'strings', 'user', 'active',]
    search_fields = ['id', 'user__username']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Brand, BrandAdmin)
admin.site.register(Instrument, InstrumentAdmin)

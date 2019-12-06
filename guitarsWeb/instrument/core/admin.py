from django.contrib import admin
from .models import Instrument

# Register your models here.

#admin.site.register(InstrumentLost)
@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brand', 'strings', 'user', 'active',]
    search_fields = ['id', 'user__username']



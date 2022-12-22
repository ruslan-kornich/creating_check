from django.contrib import admin

from .models import Check, Printer

admin.site.register(Printer)

admin.site.register(Check)

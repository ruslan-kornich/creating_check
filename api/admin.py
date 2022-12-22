from django.contrib import admin

from .models import Check, Printer


class PrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'api_key', 'check_type', 'point_id')
    ordering = ('id',)
    list_display_links = ('id', 'name',)
    search_fields = ('point_id',)
    list_filter = ('point_id',)


admin.site.register(Printer, PrinterAdmin)


class CheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'printer', 'type', 'order', 'status', 'pdf_file')
    ordering = ('id',)
    list_display_links = ('id',)
    list_filter = ('printer', 'type', 'status',)


admin.site.register(Check, CheckAdmin)

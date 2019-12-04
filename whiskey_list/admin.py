from django.contrib import admin
from .models import Spirit

# Register your models here.

class SpiritAdmin(admin.ModelAdmin):
    search_fields = ('distillery', 'brand', 'release', )


admin.site.site_header = "Whiskey House Admin"
admin.site.site_title = "Whiskey House Admin"
admin.site.index_title = "Whiskey House Admin"
admin.site.register(Spirit, SpiritAdmin)
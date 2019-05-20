from django.contrib import admin
from . import models

@admin.register(models.Thing)
class ThingAdmin(admin.ModelAdmin):
    """
    An admin interface class for the Thing model.
    """
    list_display = ('slug', 'header', 'display_order')
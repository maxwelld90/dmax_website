from django.contrib import admin
from . import models

@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    """
    An admin interface class for the Publication model.
    """
    published_date = 'year'
    empty_value_display = '(Blank)'
    list_display = ('title', 'publication_type', 'published_date')

@admin.register(models.PublicationResource)
class PublicationResourceAdmin(admin.ModelAdmin):
    """
    An admin interface class for the PublicationResource model.
    """
    list_display = ['publication', 'resource_type']
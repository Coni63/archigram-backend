from django.contrib import admin
from .models import Metadata, MetadataConfig

class MetadataConfigAdmin(admin.ModelAdmin):
    pass

class MetadataAdmin(admin.ModelAdmin):
    pass

admin.site.register(MetadataConfig, MetadataConfigAdmin)
admin.site.register(Metadata, MetadataAdmin)
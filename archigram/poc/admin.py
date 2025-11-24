from django.contrib import admin
from .models import POCModel

# Register your models here.
class POCAdmin(admin.ModelAdmin):
    pass

admin.site.register(POCModel, POCAdmin)
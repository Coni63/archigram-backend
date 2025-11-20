from django.contrib import admin
from .models import EdgeType, Edge


class EdgeTypeAdmin(admin.ModelAdmin):
    pass


class EdgeAdmin(admin.ModelAdmin):
    pass


admin.site.register(EdgeType, EdgeTypeAdmin)
admin.site.register(Edge, EdgeAdmin)
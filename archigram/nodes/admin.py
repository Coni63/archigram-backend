from django.contrib import admin
from .models import Node, NodeType

class NodeTypeAdmin(admin.ModelAdmin):
    pass

class NodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(NodeType, NodeTypeAdmin)
admin.site.register(Node, NodeAdmin)
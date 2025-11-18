from django.db import models


class NodeType(models.Model):
    """User-defined node types (docker-linux, kafka, postgres-db, etc.)"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon identifier for frontend")
    color = models.CharField(max_length=7, blank=True, help_text="Hex color code (e.g., #FF5733)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name


class Node(models.Model):
    """Represents a node in the graph (service, database, kafka, etc.)"""
    
    # Data fields
    node_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    type = models.ForeignKey(NodeType, on_delete=models.PROTECT, related_name='nodes')
    metadatas = models.JSONField(default=dict, blank=True)
    
    # Position fields
    position_x = models.FloatField()
    position_y = models.FloatField()
    
    # Optional: for organizing nodes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['node_id']
        indexes = [
            models.Index(fields=['node_id']),
            models.Index(fields=['type']),
        ]
    
    def __str__(self):
        return f"{self.node_id} - {self.label}"
from django.db import models

from metadata.models import Metadata, MetadataConfig
from nodes.models import Node
from django.contrib.contenttypes.fields import GenericRelation

class EdgeType(models.Model):
    """User-defined node types (docker-linux, kafka, postgres-db, etc.)"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    metadatas = GenericRelation(MetadataConfig)
    
    # Styling attributes
    
    class Meta:
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name


class Edge(models.Model):
    """Represents an edge/connection between nodes"""
    id = models.AutoField(primary_key=True)
    # Relationships
    source = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='outgoing_edges',
        to_field='node_id'
    )
    target = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name='incoming_edges',
        to_field='node_id'
    )
    
    # Data fields
    label = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey(EdgeType, on_delete=models.PROTECT, related_name='edges')
    metadatas = GenericRelation(Metadata)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['source', 'target']),
        ]
    
    def __str__(self):
        return f"{self.source.node_id} → {self.target.node_id}"
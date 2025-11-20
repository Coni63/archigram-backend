from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class MetadataConfig(models.Model):
    property_name = models.CharField(max_length=100)
    default_value = models.CharField(max_length=255)
    sensitive = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    group = models.CharField(max_length=100, blank=True)
    param_type = models.CharField(max_length=20, choices=[
        ('string', 'String'),
        ('integer', 'Integer'),
        ('decimal', 'Decimal'),
        ('boolean', 'Boolean'),
        ('date', 'Date'),
    ])

    # Generic Foreign Key fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        unique_together = ['content_type', 'object_id', 'property_name']
        indexes = [models.Index(fields=['content_type', 'object_id', 'property_name'])]
        ordering = ['group', 'display_order', 'property_name']


class Metadata(models.Model):
    metadata = models.ForeignKey(MetadataConfig, on_delete=models.PROTECT)
    value = models.CharField(max_length=255)
    
    # Generic Foreign Key fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ['content_type', 'object_id', 'metadata']
        indexes = [models.Index(fields=['content_type', 'object_id', 'metadata'])]
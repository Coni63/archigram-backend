from rest_framework import viewsets

from .models import Metadata, MetadataConfig
from .serializers import MetadataSerializer, MetadataConfigSerializer

class MetadataViewSet(viewsets.ModelViewSet):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class MetadataConfigViewSet(viewsets.ModelViewSet):
    queryset = MetadataConfig.objects.all()
    serializer_class = MetadataConfigSerializer

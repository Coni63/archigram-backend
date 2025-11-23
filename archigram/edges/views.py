from rest_framework import viewsets

from .models import Edge, EdgeType
from .serializers import EdgeSerializer, EdgeTypeSerializer

class EdgesViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer


class EdgeTypesViewSet(viewsets.ModelViewSet):
    queryset = EdgeType.objects.all()
    serializer_class = EdgeTypeSerializer

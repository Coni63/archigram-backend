from rest_framework import viewsets

from .models import Node, NodeType
from .serializers import NodeSerializer, NodeTypeSerializer

class NodesViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeTypesViewSet(viewsets.ModelViewSet):
    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer

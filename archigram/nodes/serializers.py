from rest_framework import serializers

from .models import Node, NodeType



class NodeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeType
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    type = NodeTypeSerializer('type', read_only=True)
    class Meta:
        model = Node
        fields = '__all__'

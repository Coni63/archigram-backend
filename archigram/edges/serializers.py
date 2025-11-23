from rest_framework import serializers

from .models import Edge, EdgeType


class EdgeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdgeType
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):
    type = EdgeTypeSerializer('type', read_only=True)

    class Meta:
        model = Edge
        fields = '__all__'
from rest_framework import serializers
from .models import POCModel

class POCSerializer(serializers.ModelSerializer):
    version = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = POCModel
        fields = ['id', 'project', 'version', 'data', 'created_at']
        read_only_fields = ['version', 'created_at']
from rest_framework import serializers

from .models import Metadata, MetadataConfig


class MetadataConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataConfig
        fields = '__all__'


class MetadataSerializer(serializers.ModelSerializer):
    metadata = MetadataConfigSerializer('metadata', read_only=True)

    class Meta:
        model = Metadata
        fields = '__all__'
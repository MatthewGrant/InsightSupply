from rest_framework import serializers
from notes import models


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.StringRelatedField()
    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'color',
        )

# nested category inside each Insight object
class InsightSerializer(serializers.ModelSerializer):
    id = serializers.StringRelatedField()
    category = CategorySerializer()

    class Meta:
        model = models.Insight
        fields = (
            'id',
            'caption',
            'category',
            'source_url',
            'created_at',
        )

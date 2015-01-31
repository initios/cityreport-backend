from rest_framework import serializers, fields

from . import models


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue

    postal_code = fields.CharField(read_only=True)
    city = fields.CharField(read_only=True)
    state = fields.CharField(read_only=True)
    county = fields.CharField(read_only=True)
    country = fields.CharField(read_only=True)
    type = serializers.PrimaryKeyRelatedField(queryset=models.Type.objects.all())
    type_nested = TypeSerializer(read_only=True, source='type')

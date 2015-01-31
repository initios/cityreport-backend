from rest_framework import serializers

from . import models


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Type


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Issue
        exclude = ('postal_code', 'city', 'county', 'country')

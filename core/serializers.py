from rest_framework import serializers

from . import models


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Issue
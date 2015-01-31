from rest_framework import viewsets

from . import models, serializers


class IssueViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


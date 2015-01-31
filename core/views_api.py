from rest_framework import viewsets, mixins

from . import models, serializers


class IssueViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


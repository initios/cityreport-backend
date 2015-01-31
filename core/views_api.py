from rest_framework import viewsets

from . import models, serializers


class IssueViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer



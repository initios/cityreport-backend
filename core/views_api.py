from django.db.models import Count

from rest_framework import viewsets, mixins, views
from rest_framework.response import Response

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


class BulkIssueViewSet(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class TopCitiesStatsView(views.APIView):
    def get(self, request, format=None):
        data = models.Issue.objects.values('city').order_by('-matches').annotate(matches=Count('city'))[:10]
        return Response(data, 200)

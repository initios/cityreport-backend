from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from core import views_api

router = DefaultRouter()
router.register(r'issues', views_api.IssueViewSet)

urlpatterns = patterns(
    '',
    url(r'^api-rest/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from core import views_api, views

router = DefaultRouter()
router.register(r'types', views_api.TypeViewSet)
router.register(r'issues', views_api.IssueViewSet)


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^api-rest/top/cities/$', views_api.TopCitiesStatsView.as_view(), name='top_cities'),
    url(r'^api-rest/top/counties/$', views_api.TopCountiesStatsView.as_view(), name='top_counties'),
    url(r'^api-rest/populate/$', 'core.views_api.populate', name='populate'),
    url(r'^api-rest/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

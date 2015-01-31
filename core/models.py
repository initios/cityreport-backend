from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel


class Type(TimeStampedModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255, blank=False, null=False)


class Issue(TimeStampedModel):
    type = models.ForeignKey(Type, verbose_name=_('Type'))

    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'))
    location = models.CharField(verbose_name=_('Location'), max_length=255, blank=False, null=False)
    state = models.CharField(verbose_name=_('State'), max_length=255, blank=False, null=False)


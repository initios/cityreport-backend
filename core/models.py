from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel


class Type(TimeStampedModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)


class Issue(TimeStampedModel):
    type = models.ForeignKey(Type, verbose_name=_('Type'))

    lat = models.FloatField(_('Latitude'))
    lon = models.FloatField(_('Longitude'))
    description = models.TextField(verbose_name=_('Description'))
    location = models.CharField(verbose_name=_('Location'), max_length=255)
    state = models.CharField(verbose_name=_('State'), max_length=255)


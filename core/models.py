from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel


class Type(TimeStampedModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __str__(self):
        return self.name


class Issue(TimeStampedModel):
    type = models.ForeignKey(Type, verbose_name=_('Type'))

    lat = models.FloatField(_('Latitude'))
    lon = models.FloatField(_('Longitude'))
    description = models.TextField(verbose_name=_('Description'))
    location = models.CharField(verbose_name=_('Location'), max_length=255)
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=255, blank=False)
    city = models.CharField(verbose_name=_('City'), max_length=255, blank=False)
    state = models.CharField(verbose_name=_('State'), max_length=255, blank=False)
    county = models.CharField(verbose_name=_('County'), max_length=255, blank=False)
    country = models.CharField(verbose_name=_('Country'), max_length=255, blank=False)

    def __str__(self):
        return self.description

from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel

from . import services

class Type(TimeStampedModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __str__(self):
        return self.name


class Issue(TimeStampedModel):
    type = models.ForeignKey(Type, verbose_name=_('Type'))

    lat = models.FloatField(_('Latitude'))
    lon = models.FloatField(_('Longitude'))
    description = models.TextField(verbose_name=_('Description'))
    postal_code = models.CharField(verbose_name=_('Postal Code'), max_length=255, blank=False)
    city = models.CharField(verbose_name=_('City'), max_length=255, blank=False)
    state = models.CharField(verbose_name=_('State'), max_length=255, blank=False)
    county = models.CharField(verbose_name=_('County'), max_length=255, blank=False)
    country = models.CharField(verbose_name=_('Country'), max_length=255, blank=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if force_update is True or update_fields is True or self.postal_code == '' or self.postal_code is None:
            geodata = services.reverse_geocode(self.lat, self.lon)

            for key, value in geodata.items():
                setattr(self, key, value)

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.description

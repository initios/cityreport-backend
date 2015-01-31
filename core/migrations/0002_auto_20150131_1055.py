# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_issues_types(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Type = apps.get_model("core", "Type")
    types = ('vandalism', 'noise polution', 'crime', 'disturb', 'crash', 'terrorism', 'strike', 'natural disaster')
    Type.objects.bulk_create([Type(name=name) for name in types])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_issues_types),
    ]

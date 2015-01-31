# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_type_default(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Type = apps.get_model("core", "Type")
    Type.objects.bulk_create([Type(name=name) for name in ('default', )])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_issue_address'),
    ]

    operations = [
        migrations.RunPython(add_type_default),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150131_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='address',
            field=models.TextField(verbose_name='Dirección', default=''),
            preserve_default=False,
        ),
    ]

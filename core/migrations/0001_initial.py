# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('description', models.TextField(verbose_name='Description')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(verbose_name='Type', to='core.Type'),
            preserve_default=True,
        ),
    ]

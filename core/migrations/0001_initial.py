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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('description', models.TextField(verbose_name='Description')),
                ('postal_code', models.CharField(verbose_name='Postal Code', max_length=255)),
                ('city', models.CharField(verbose_name='City', max_length=255)),
                ('state', models.CharField(verbose_name='State', max_length=255)),
                ('county', models.CharField(verbose_name='County', max_length=255)),
                ('country', models.CharField(verbose_name='Country', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
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

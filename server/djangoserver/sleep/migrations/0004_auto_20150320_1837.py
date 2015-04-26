# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0003_auto_20150318_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleepsession',
            name='session_end',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sleepsession',
            name='session_start',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sleepsession',
            name='avg_respiration_rate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

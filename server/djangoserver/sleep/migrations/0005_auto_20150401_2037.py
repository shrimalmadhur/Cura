# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0004_auto_20150320_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsdata',
            name='sleep_session',
            field=models.ForeignKey(related_name='time_series_data', to='sleep.SleepSession'),
            preserve_default=True,
        ),
    ]

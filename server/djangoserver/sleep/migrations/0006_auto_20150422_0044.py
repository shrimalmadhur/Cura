# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0005_auto_20150401_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsdata',
            name='data_type',
            field=models.IntegerField(choices=[(1, b'Sleep Stage'), (2, b'Snoring Episode'), (3, b'Sleep Cycle'), (4, b'Heart Rate'), (5, b'Presence')]),
            preserve_default=True,
        ),
    ]

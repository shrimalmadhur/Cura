# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercredential',
            name='id',
        ),
        migrations.AlterField(
            model_name='sleepsession',
            name='bath_count',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tsdata',
            name='data_type',
            field=models.IntegerField(choices=[(1, b'Sleep Stage'), (2, b'Snoring Episode'), (3, b'Sleep Cycle'), (3, b'Heart Rate'), (5, b'Presence')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercredential',
            name='user',
            field=models.OneToOneField(related_name='beddit_credential', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

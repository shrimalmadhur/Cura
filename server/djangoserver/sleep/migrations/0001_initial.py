# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SleepSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('sleep_time_target', models.PositiveIntegerField(null=True, blank=True)),
                ('rest_heart_rate', models.PositiveIntegerField(null=True, blank=True)),
                ('avg_respiration_rate', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('sleep_latency', models.PositiveIntegerField(null=True, blank=True)),
                ('total_snore_duration', models.PositiveIntegerField(null=True, blank=True)),
                ('away_count', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('bath_count', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('stage_duration_A', models.PositiveIntegerField(null=True, blank=True)),
                ('stage_duration_S', models.PositiveIntegerField(null=True, blank=True)),
                ('stage_duration_R', models.PositiveIntegerField(null=True, blank=True)),
                ('stage_duration_W', models.PositiveIntegerField(null=True, blank=True)),
                ('stage_duration_G', models.PositiveIntegerField(null=True, blank=True)),
                ('score_amount_sleep', models.SmallIntegerField(null=True, blank=True)),
                ('score_bed_exits', models.SmallIntegerField(null=True, blank=True)),
                ('score_snoring', models.SmallIntegerField(null=True, blank=True)),
                ('score_sleep_latency', models.SmallIntegerField(null=True, blank=True)),
                ('score_sleep_efficiency', models.SmallIntegerField(null=True, blank=True)),
                ('score_awakening', models.SmallIntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TSData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_type', models.IntegerField(choices=[(1, b'Sleep Stage'), (2, b'Snoring Episode'), (3, b'Sleep Cycle'), (3, b'Heart Rate')])),
                ('timestamp', models.DateTimeField()),
                ('value', models.FloatField()),
                ('sleep_session', models.ForeignKey(to='sleep.SleepSession')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=256, null=True, blank=True)),
                ('beddit_id', models.CharField(max_length=32, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

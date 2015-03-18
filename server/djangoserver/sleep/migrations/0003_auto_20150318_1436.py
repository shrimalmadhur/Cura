# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sleep', '0002_auto_20150317_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercredential',
            name='beddit_id',
        ),
        migrations.RemoveField(
            model_name='usercredential',
            name='token',
        ),
        migrations.AddField(
            model_name='usercredential',
            name='password',
            field=encrypted_fields.fields.EncryptedTextField(default=''),
            preserve_default=False,
        ),
    ]

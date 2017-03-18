# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170317_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
        migrations.AlterField(
            model_name='note',
            name='username',
            field=models.ForeignKey(to='web.User'),
        ),
    ]

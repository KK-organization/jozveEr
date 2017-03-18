# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20170318_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='username',
            field=models.ForeignKey(to='web.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='signedin',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]

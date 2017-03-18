# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170318_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signedin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='username',
            field=models.ForeignKey(to='web.User'),
        ),
    ]

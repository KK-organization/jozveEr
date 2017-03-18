# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170317_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='note',
            name='username',
            field=models.ForeignKey(to='web.User'),
        ),
    ]

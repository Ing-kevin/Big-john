# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0006_auto_20151123_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

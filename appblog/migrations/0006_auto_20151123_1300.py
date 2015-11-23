# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0005_auto_20151123_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='fecha',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='img',
            field=models.URLField(),
        ),
    ]

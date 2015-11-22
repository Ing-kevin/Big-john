# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0002_auto_20151026_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='autor',
            field=models.IntegerField(choices=[(1, b'Barranquilla'), (2, b'Cali'), (3, b'Bogota'), (4, b'Cucuta')]),
            preserve_default=False,
        ),
    ]

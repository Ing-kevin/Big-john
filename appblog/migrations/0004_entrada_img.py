# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0003_entrada_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='img',
            field=models.ImageField(upload_to=b'imgenes'),
            preserve_default=False,
        ),
    ]

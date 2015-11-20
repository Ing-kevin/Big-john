# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_removed_unique_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_slug',
            field=models.SlugField(default='new'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='query',
            name='query_slug',
            field=models.SlugField(default='old'),
            preserve_default=False,
        ),
    ]

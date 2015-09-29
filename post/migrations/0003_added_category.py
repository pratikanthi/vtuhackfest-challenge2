# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_added_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_cat',
            field=models.ManyToManyField(related_name='category', to='post.Category'),
        ),
    ]

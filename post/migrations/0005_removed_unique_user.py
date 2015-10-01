# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_added_answer_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

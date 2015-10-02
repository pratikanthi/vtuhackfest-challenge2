# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_added_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

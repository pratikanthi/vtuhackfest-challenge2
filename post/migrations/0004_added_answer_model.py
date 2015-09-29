# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_added_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.TextField()),
                ('answer_date', models.DateTimeField(default=datetime.datetime.now)),
                ('answer_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
                ('answer_to_query', models.ForeignKey(to='post.Query')),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
    ]

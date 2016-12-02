# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20161201_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reviewed_by',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='reviews'),
        ),
    ]

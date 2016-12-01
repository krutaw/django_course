# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, help_text='Use pen name, not real name', max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='Favorite?'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author', related_name='books'),
        ),
    ]

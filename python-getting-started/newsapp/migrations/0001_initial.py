# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-08 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date_published')),
                ('nltk_score', models.FloatField(default=0)),
                ('nltk_score_title', models.FloatField(default=0)),
                ('source', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date_published')),
                ('currency', models.FloatField(default=0)),
                ('peso', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date_published')),
                ('close', models.FloatField(default=0)),
                ('ticker', models.TextField()),
            ],
        ),
    ]

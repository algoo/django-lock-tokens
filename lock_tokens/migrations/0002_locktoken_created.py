# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("lock_tokens", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="locktoken",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_docs', to='courses.Course'),
            preserve_default=False,
        ),
    ]

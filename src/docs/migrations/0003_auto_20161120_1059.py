# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_document_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_docs', to='courses.Course', verbose_name='Курс'),
        ),
    ]

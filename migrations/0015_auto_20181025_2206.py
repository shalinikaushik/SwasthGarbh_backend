# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swasthGarbhApp', '0014_auto_20181024_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cvd_portal.Patient'),
        ),
    ]
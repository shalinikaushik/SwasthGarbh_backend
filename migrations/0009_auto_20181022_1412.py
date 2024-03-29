# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-22 08:42
from __future__ import unicode_literals

import cvd_portal.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swasthGarbhApp', '0008_auto_20180620_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregnancydata',
            name='abdominal_pain',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='bleeding_per_vaginum',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='decreased_fetal_movements',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='headache',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='swelling_in_hands_or_face',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='urine_albumin',
        ),
        migrations.RemoveField(
            model_name='pregnancydata',
            name='visual_problems',
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_extra_comments',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_period',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_time_of_day',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_timespan_days',
            field=models.IntegerField(default=7),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_anemia',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_hiv',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_tetnus',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_ultrasound',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc1_urine',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc2_anemia',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc2_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc2_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc2_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc3_anemia',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc3_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc3_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc3_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc3_urine',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc4_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc4_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc4_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc5_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc5_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc5_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc5_urine',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc6_anemia',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc6_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc6_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc6_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc7_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc7_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc7_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc8_diabtese',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc8_dueDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='anc8_safeDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pregnancydata',
            name='startDate',
            field=cvd_portal.models.CustomDateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_Image',
            field=models.TextField(default=''),
        ),
    ]

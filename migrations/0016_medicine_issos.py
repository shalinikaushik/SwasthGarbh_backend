# Generated by Django 2.1.5 on 2019-02-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swasthGarbhApp', '0015_auto_20181025_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='isSOS',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_exhibit', '0003_auto_20161012_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitentry',
            name='image',
            field=models.ImageField(upload_to='images/code_exhibit/'),
        ),
    ]

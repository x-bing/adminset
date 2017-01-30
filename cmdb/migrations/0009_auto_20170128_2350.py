# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-28 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0008_auto_20161006_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='product',
            new_name='group',
        ),
        migrations.AddField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_model',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='memory',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='os',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='sn',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='host',
            name='vendor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
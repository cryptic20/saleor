# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0006_auto_20171109_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingmethod',
            options={'permissions': (('view_shipping', 'Can views shipping method'), ('edit_shipping', 'Can edit shipping method'))},
        ),
        migrations.AlterModelOptions(
            name='shippingmethodcountry',
            options={},
        ),
    ]

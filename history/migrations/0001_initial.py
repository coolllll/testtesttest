# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-29 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='order date')),
                ('status', models.CharField(default='on hold', max_length=50)),
                ('shipMethodID', models.IntegerField(default='0')),
                ('payMethod', models.CharField(default='credit card', max_length=50)),
                ('trackingNo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('ordItemsID', models.AutoField(primary_key=True, serialize=False)),
                ('productID', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('sumPrice', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Order')),
            ],
        ),
    ]
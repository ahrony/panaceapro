# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procurement', '0009_auto_20150331_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetRepair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
                ('designation', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('repair_complete_date', models.CharField(max_length=128, verbose_name=b'Recommended Repair Completion Date')),
                ('manager', models.CharField(max_length=128, verbose_name=b'Manager/Team Leader')),
                ('procure_manager', models.CharField(max_length=128, verbose_name=b'Manager procurement Department')),
                ('chief_officer', models.CharField(max_length=128, verbose_name=b'Chief Executive Officer')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RepairItemDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_no', models.IntegerField(max_length=30)),
                ('item_name', models.CharField(max_length=128, verbose_name=b'Name of equipment in need of repair')),
                ('detail', models.TextField(max_length=1000, verbose_name=b'Details description of malfunction in need of repair')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_model', models.ForeignKey(to='procurement.AssetRepair')),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

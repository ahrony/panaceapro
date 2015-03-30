# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContraVoucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('voucher_no', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('paid_amount', models.TextField(max_length=1000, verbose_name=b'Being the amount paid for')),
                ('amount_in_words', models.TextField(max_length=1000, verbose_name=b'Amount in words')),
                ('prepare_by', models.CharField(max_length=128)),
                ('chief_officer', models.CharField(max_length=128, verbose_name=b'Chief Executive Officer')),
                ('certified_by', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LedgerVoucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('voucher', models.ForeignKey(to='procurement.ContraVoucher')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoucherDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('ledger_info', models.IntegerField(max_length=128, verbose_name=b'Ledger Folio')),
                ('debit_info', models.IntegerField(max_length=128, verbose_name=b'DEBIT')),
                ('credit_info', models.IntegerField(max_length=128, verbose_name=b'CREDIT')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

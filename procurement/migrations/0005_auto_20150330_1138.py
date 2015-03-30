# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procurement', '0004_auto_20150330_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContraDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('ledger_info', models.IntegerField(max_length=128, verbose_name=b'Ledger Folio')),
                ('debit_info', models.IntegerField(max_length=128, verbose_name=b'DEBIT')),
                ('credit_info', models.IntegerField(max_length=128, verbose_name=b'CREDIT')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_model', models.ForeignKey(to='procurement.ContraVoucher', null=True)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('ledger_info', models.IntegerField(max_length=128, verbose_name=b'Ledger Folio')),
                ('debit_info', models.IntegerField(max_length=128, verbose_name=b'DEBIT')),
                ('credit_info', models.IntegerField(max_length=128, verbose_name=b'CREDIT')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditVoucher',
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
            name='DebitDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('ledger_info', models.IntegerField(max_length=128, verbose_name=b'Ledger Folio')),
                ('debit_info', models.IntegerField(max_length=128, verbose_name=b'DEBIT')),
                ('credit_info', models.IntegerField(max_length=128, verbose_name=b'CREDIT')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DebitVoucher',
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
            name='LedgerDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_head', models.CharField(max_length=128, verbose_name=b'Certified/Accounts')),
                ('ledger_info', models.IntegerField(max_length=128, verbose_name=b'Ledger Folio')),
                ('debit_info', models.IntegerField(max_length=128, verbose_name=b'DEBIT')),
                ('credit_info', models.IntegerField(max_length=128, verbose_name=b'CREDIT')),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent_model', models.ForeignKey(to='procurement.LedgerVoucher', null=True)),
                ('updated_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='voucherdetail',
            name='contra_model',
        ),
        migrations.RemoveField(
            model_name='voucherdetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='voucherdetail',
            name='ledger_model',
        ),
        migrations.RemoveField(
            model_name='voucherdetail',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='VoucherDetail',
        ),
        migrations.AddField(
            model_name='debitdetail',
            name='parent_model',
            field=models.ForeignKey(to='procurement.DebitVoucher', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='debitdetail',
            name='updated_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creditdetail',
            name='parent_model',
            field=models.ForeignKey(to='procurement.CreditVoucher', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creditdetail',
            name='updated_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

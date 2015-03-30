# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0005_auto_20150330_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contravoucher',
            old_name='prepare_by',
            new_name='prepared_by',
        ),
        migrations.RenameField(
            model_name='creditvoucher',
            old_name='prepare_by',
            new_name='prepared_by',
        ),
        migrations.RenameField(
            model_name='debitvoucher',
            old_name='prepare_by',
            new_name='prepared_by',
        ),
        migrations.RenameField(
            model_name='ledgervoucher',
            old_name='prepare_by',
            new_name='prepared_by',
        ),
        migrations.AlterField(
            model_name='contradetail',
            name='account_head',
            field=models.CharField(max_length=128, verbose_name=b'Head of Account'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creditdetail',
            name='account_head',
            field=models.CharField(max_length=128, verbose_name=b'Head of Account'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='debitdetail',
            name='account_head',
            field=models.CharField(max_length=128, verbose_name=b'Head of Account'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ledgerdetail',
            name='account_head',
            field=models.CharField(max_length=128, verbose_name=b'Head of Account'),
            preserve_default=True,
        ),
    ]

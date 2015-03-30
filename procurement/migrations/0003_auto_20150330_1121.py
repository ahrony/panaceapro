# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0002_voucherdetail_parrent_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgervoucher',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='ledgervoucher',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='ledgervoucher',
            name='voucher',
        ),
        migrations.DeleteModel(
            name='LedgerVoucher',
        ),
        migrations.RemoveField(
            model_name='voucherdetail',
            name='parrent_model',
        ),
        migrations.AddField(
            model_name='voucherdetail',
            name='contra_model',
            field=models.ForeignKey(related_name='contra_model', to='procurement.ContraVoucher', null=True),
            preserve_default=True,
        ),
    ]

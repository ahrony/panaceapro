# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucherdetail',
            name='parrent_model',
            field=models.ForeignKey(to='procurement.ContraVoucher', null=True),
            preserve_default=True,
        ),
    ]

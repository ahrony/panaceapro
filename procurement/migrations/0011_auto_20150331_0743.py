# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0010_assetrepair_repairitemdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contradetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='contradetail',
            name='parent_model',
        ),
        migrations.RemoveField(
            model_name='contradetail',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='ContraDetail',
        ),
        migrations.RemoveField(
            model_name='contravoucher',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='contravoucher',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='ContraVoucher',
        ),
        migrations.RemoveField(
            model_name='creditdetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='creditdetail',
            name='parent_model',
        ),
        migrations.RemoveField(
            model_name='creditdetail',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='CreditDetail',
        ),
        migrations.RemoveField(
            model_name='creditvoucher',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='creditvoucher',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='CreditVoucher',
        ),
        migrations.RemoveField(
            model_name='debitdetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='debitdetail',
            name='parent_model',
        ),
        migrations.RemoveField(
            model_name='debitdetail',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='DebitDetail',
        ),
        migrations.RemoveField(
            model_name='debitvoucher',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='debitvoucher',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='DebitVoucher',
        ),
        migrations.RemoveField(
            model_name='journaldetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='journaldetail',
            name='parent_model',
        ),
        migrations.RemoveField(
            model_name='journaldetail',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='JournalDetail',
        ),
        migrations.RemoveField(
            model_name='journalvoucher',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='journalvoucher',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='JournalVoucher',
        ),
        migrations.AlterField(
            model_name='repairitemdetail',
            name='detail',
            field=models.TextField(max_length=500, verbose_name=b'Details description of malfunction in need of repair'),
            preserve_default=True,
        ),
    ]

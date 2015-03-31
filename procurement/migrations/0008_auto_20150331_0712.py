# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0007_auto_20150331_0659'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='contradetail',
            name='journal',
            field=models.ForeignKey(to='procurement.JournalVoucher', null=True),
            preserve_default=True,
        ),
    ]

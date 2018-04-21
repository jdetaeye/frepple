# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 05:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0023_transferbatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='quantity',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=15, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='operationmaterial',
            name='type',
            field=models.CharField(blank=True, choices=[('start', 'Start'), ('end', 'End'), ('fixed_start', 'Fixed start'), ('fixed_end', 'Fixed end'), ('transfer_batch', 'Batch transfer')], default='start', help_text='Consume/produce material at the start or the end of the operationplan', max_length=20, null=True, verbose_name='type'),
        ),
        # migrations.AlterField(
        #     model_name='operationplanresource',
        #     name='resource',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operationplanresources', to='input.Resource', verbose_name='resource'),
        # ),
        migrations.AlterField(
            model_name='setuprule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='identifier'),
        ),
    ]

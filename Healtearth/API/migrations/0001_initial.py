# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('amount', models.DecimalField(max_digits=7, decimal_places=2)),
                ('unit', models.CharField(max_length=10)),
                ('air_pollution', models.DecimalField(max_digits=10, decimal_places=2)),
                ('water_pollution', models.DecimalField(max_digits=10, decimal_places=2)),
                ('garbage', models.DecimalField(max_digits=10, decimal_places=2)),
                ('grade', models.CharField(max_length=1)),
                ('alternatives', models.ManyToManyField(related_name='alternatives_rel_+', to='API.Food')),
            ],
        ),
    ]

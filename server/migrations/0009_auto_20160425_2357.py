# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20150814_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='serial',
            field=models.CharField(unique=True, max_length=200, verbose_name=b'Serial Number'),
        ),
    ]

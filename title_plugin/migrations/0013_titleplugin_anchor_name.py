# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title_plugin', '0012_titleicon_vector_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='titleplugin',
            name='anchor_name',
            field=models.CharField(max_length=250, null=True, verbose_name='Custom Anchor Name', blank=True),
        ),
    ]

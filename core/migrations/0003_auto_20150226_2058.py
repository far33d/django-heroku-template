# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150226_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitem',
            name='icon_url',
            field=models.FilePathField(path=b'/static/icons'),
            preserve_default=True,
        ),
    ]

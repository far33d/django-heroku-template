# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitem',
            name='icon_url',
            field=models.FilePathField(path=b'/Users/fareed/src/cokitchen/cokitchen/../core/static/icons'),
            preserve_default=True,
        ),
    ]

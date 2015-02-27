# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150226_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserecord',
            name='customer_email',
            field=models.EmailField(default='far33d@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='stripe_token',
            field=models.CharField(default='OLD', max_length=32),
            preserve_default=False,
        ),
    ]

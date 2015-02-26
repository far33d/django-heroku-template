import os

from django.db import models
from cokitchen import settings

class TestItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    icon_url = models.CharField(max_length=100)

    def __unicode__(self):
        return 'TestItem: %s, $%d' % (self.name, self.price)

class PurchaseRecord(models.Model):
    item = models.ForeignKey(TestItem)
    purchase_time = models.DateTimeField(auto_now_add=True)



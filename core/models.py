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

    def price_cents(self):
        return int(self.price * 100)

class PurchaseRecord(models.Model):
    item = models.ForeignKey(TestItem)
    purchase_time = models.DateTimeField(auto_now_add=True)
    customer_email = models.EmailField(max_length=254)
    stripe_token = models.CharField(max_length=32)

    def __unicode__(self):
        return 'customer: %s purchase: %s' % (self.customer_email, self.item.name)

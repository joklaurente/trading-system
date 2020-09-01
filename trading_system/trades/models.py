from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    oid = models.CharField("Object ID", unique=True, max_length=200)
    name = models.CharField("Stock Name", max_length=200)
    price = models.DecimalField("Stock Price", max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Trade(models.Model):
    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='+')
    stock = models.ForeignKey(
        Stock, null=True, on_delete=models.SET_NULL, related_name='+')
    quantity = models.IntegerField("Stock quantity", default=1)

    def __str__(self):
        return '%s: %s' % (self.user, self.stock)

    def get_total(self):
        return self.stock.price * self.quantity

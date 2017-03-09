from django.db import models
from django.contrib.auth.models import User


class Actual(models.Model):
    name = models.CharField(max_length=10, default='A1')

    class Meta:
        verbose_name = ('Actual')
        verbose_name_plural = ('Actuales')

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=10, default='C1')

    class Meta:
        verbose_name = ('Currency')
        verbose_name_plural = ('Currencys')

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    currency = models.ForeignKey(Currency, blank=True, null=True)
    amount = models.IntegerField()

    class Meta:
        verbose_name = ('Account')
        verbose_name_plural = ('Accounts')

    def __str__(self):
        return self.amount

    def withdraw(self, amount, target):
        assert self.amount >= amount
        assert self.currency.name == target.currency.name
        self.amount -= amount
        target.amount += amount

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


class Categories(models.Model):
    """Categories"""
    name = models.CharField("name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Items(models.Model):
    """Items"""
    name = models.CharField("name", max_length=100)
    price = models.PositiveSmallIntegerField("price", default=0)
    category = models.ForeignKey(Categories, verbose_name="Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Purchases(models.Model):
    """Purchases"""
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    item = models.ForeignKey(Items, verbose_name="Item", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '_' + self.item.name + '_' + self.date.date().__str__()

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.utils import timezone


class Categories(models.Model):
    """Categories"""
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Items(models.Model):
    """Items"""
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    item = models.ForeignKey(Items, verbose_name="Item", on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username + '_' + self.item.name + '_' + self.date.__str__() + '_' + self.item.price.__str__()

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(name="first_name", max_length=50)
    surname = models.CharField(name="last_name", max_length=50)
    email = models.EmailField(name="email", max_length=120)
    message = models.TextField(name="message")

    def __str__(self):
        return self.id.__str__() + '_' + self.name + '_' + self.surname + '_' + self.email


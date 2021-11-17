from django.db import models


class Roles(models.Model):
    """Roles"""
    name = models.CharField("name", max_length=150)


class Users(models.Model):
    """Users"""
    name = models.CharField("name", max_length=100)
    surname = models.CharField("surname", max_length=100)
    email = models.EmailField()
    password = models.CharField("password", max_length=10)
    role = models.ForeignKey(Roles, verbose_name="Role", on_delete=models.CASCADE)


class Categories(models.Model):
    """Categories"""
    name = models.CharField("name", max_length=100)


class Items(models.Model):
    """Items"""
    name = models.CharField("name", max_length=100)
    price = models.PositiveSmallIntegerField("price", default=0)
    category = models.ForeignKey(Categories, verbose_name="Category", on_delete=models.CASCADE)


class Purchases(models.Model):
    """Purchases"""
    user = models.ForeignKey(Users, verbose_name="User", on_delete=models.CASCADE)
    item = models.ForeignKey(Items, verbose_name="Item", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
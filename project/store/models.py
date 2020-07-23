from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'ID: {self.id}. {self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'ID: {self.id}. {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    info = models.TextField(max_length=5000)

    def __str__(self):
        return f'ID: {self.id}. {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'ID: {self.id}, customer: {self.customer.name}{", complete" if self.complete else ""}'

    @property
    def amount(self):
        return sum(item.amount for item in self.items.all())


class OrderItem():
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='items')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return f'ID: {self.id}, order ID: {self.order.id}, product: {self.product.name}, amount: {self.amount}'

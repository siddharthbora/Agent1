from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Users(models.Model):  # extended user model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    phone = models.BigIntegerField(default=0)
    address = models.CharField(default='', max_length=50)
    gst = models.CharField(default='', max_length=15)

    def __str__(self):
        return f"{self.user.first_name} |{self.user.username}|"


class Party(models.Model):
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    phone = models.BigIntegerField(default=0)
    address = models.CharField(default='', max_length=50)
    gst = models.CharField(default='', max_length=15)
    outstanding_balance = models.FloatField(default=0)
    outstanding_brokerage = models.FloatField(default=0)


class Agent(models.Model):
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    phone = models.BigIntegerField(default=0)
    address = models.CharField(default='', max_length=50)
    gst = models.CharField(default='', max_length=15)
    outstanding_balance = models.FloatField(default=0)


class Transport(models.Model):
    name = models.CharField(default='', max_length=100)


class Viewer(models.Model):
    name = models.CharField(default='', max_length=100)


class Entry(models.Model):
    e_from = ForeignKey(Party, on_delete=models.CASCADE, related_name='e_from')
    e_to = ForeignKey(Party, on_delete=models.CASCADE, related_name='e_to')
    agent2 = ForeignKey(Agent, on_delete=models.CASCADE, related_name='agent2')
    quantity = models.CharField(default='', max_length=50)
    metrics = models.CharField(default='', max_length=50)
    rate = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    outstanding_date = models.DateField(auto_now_add=True, null=True)
    clear_date = models.CharField(default='[]', max_length=1500)
    brokerage_amount_agent = models.FloatField(default=0)
    brokerage_amount_agent2 = models.FloatField(default=0)
    transport_name = models.CharField(default="", max_length=150)
    lr_no = models.CharField(default="", max_length=150)
    viewer_name = models.CharField(default="", max_length=150)

    def __str__(self):
        return f"{self.e_from.user.username} - {self.self.e_to.user.username}"

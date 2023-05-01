from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Users(models.Model):  # extended user model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    phone = models.IntegerField(default=0)
    address = models.CharField(default='', max_length=50)
    gst = models.CharField(default='', max_length=15)
    is_agent = models.BooleanField(default='false')
    is_party = models.BooleanField(default='false')

    def __str__(self):
        return f"{self.user.first_name} |{self.user.username}|"


class Entry(models.Model):
    e_from = ForeignKey(Users, on_delete=models.CASCADE, related_name='e_from')
    e_to = ForeignKey(Users, on_delete=models.CASCADE, related_name='e_to')
    agent2 = ForeignKey(Users, on_delete=models.CASCADE, related_name='agent2')
    quality = models.CharField(default='', max_length=50)
    quantity = models.CharField(default='', max_length=50)
    metrics = models.CharField(default='', max_length=50)
    rate = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.e_from.user.username} - {self.self.e_to.user.username}"

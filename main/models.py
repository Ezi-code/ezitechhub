from django.db import models

# Create your models here.
class Contacts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(null=False, max_length=500)


class Services(models.Model):
    id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=200, default='Name of service...')
    service_description = models.TextField(default='Describe service...')
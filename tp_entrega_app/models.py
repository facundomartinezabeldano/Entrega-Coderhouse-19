from django.db import models
import datetime
import uuid
from django.utils import timezone


class Relative(models.Model):
    id = models.CharField(default=str(uuid.uuid1())[0:10],
                          max_length=10, primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    birth_date = models.DateField(default=timezone.now())

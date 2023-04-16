from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Acount(models.Model):
    number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)     #СВЯЗЬ ОДИН К ОДНОМУ(OneToOneField)
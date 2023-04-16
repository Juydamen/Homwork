#ЗДЕСЬ СОЗДАЁМ СВОИ МОДЕЛИ (подобные как в файле models у users)
from django.contrib.auth.models import User
from django.db import models

from acounts.models import Acount
from products.models import Product


# Create your models here.

class SalesObject(models.Model):
    a_1 = models.IntegerField()             #ЗАДАЁМ ПОЛЯ ДЛЯ НАШЕЙ МОДЕЛИ ЭТО( а_1 и а_2 )
    a_2 = models.CharField(max_length=255)
    a_3 = models.ForeignKey(User, on_delete=models.CASCADE, null=True)          #СВЯЗЬ МНОГИМ К ОДНОМУ(ForeignKey)
    products = models.ManyToManyField(Product)                                  #СВЯЗЬ МНОГИЕ ОК МНОГИМ(ManyToManyField)

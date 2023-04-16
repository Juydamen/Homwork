#ЗДЕСЬ МЫ РЕГИСТРИРУЕМ НАШИ МОДЕЛИ ТАК ЧТОБЫ ОНИ ОТОБРАЖАЛИСЬ НА СТРАНИЦЕ(ИНТЕРФЕЙСЕ) АДМИНИСТРАТОРА


from django.contrib import admin

from products.models import Product
from .models import SalesObject
# Register your models here.
admin.site.register(SalesObject)

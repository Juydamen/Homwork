# ЗДЕСЬ ПИШУТ ПРЕДСТАВЛЕНИЯ, ЛОГИКА ОТОБРАЖЕНИЯ ВЕБ СТРАНИЦЫ

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from objects.models import SalesObject
from objects.serializers import ObjectSerializer


# Create your views here.
def objects_page(request):  # УКАЗАЛИ НОВОЕ ПРЕДСТАВЛЕНИЕ ДЛЯ ПРИЛОЖЕНИЯ objects
    return render(request, 'index.html', {'objects': SalesObject.objects.all()})  # может быть классом или функцией


class ObjectView(ModelViewSet):
    queryset = SalesObject.objects.all()
    serializer_class = ObjectSerializer

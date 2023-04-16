from rest_framework.serializers import ModelSerializer

from objects.models import SalesObject


class ObjectSerializer(ModelSerializer):
    class Meta:
        model = SalesObject
        fields = ['a_1', 'a_2']

from consultadividas.dividas.models import Divida, Cedente, Sacado, Endereco
from rest_framework import serializers


class DividaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Divida
        fields = '__all__'


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class CedenteSerializer(serializers.HyperlinkedModelSerializer):
    dividas = DividaSerializer(read_only=True)
    class Meta:
        model = Cedente
        fields = '__all__'


class SacadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sacado
        fields = '__all__'

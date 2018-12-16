from consultadividas.dividas.models import Divida, Cedente, Sacado, Endereco
from rest_framework import viewsets
from consultadividas.dividas.serializers import DividaSerializer, CedenteSerializer, SacadoSerializer, \
    EnderecoSerializer
from django_filters import rest_framework as filters


class DividaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Divida.objects.all()
    serializer_class = DividaSerializer


class CedenteFilter(filters.FilterSet):
    class Meta:
        model = Cedente
        fields = '__all__'


class CedenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Divida.objects.all()
    queryset = Cedente.objects.all()
    serializer_class = CedenteSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CedenteFilter


class SacadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sacado.objects.all()
    serializer_class = SacadoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

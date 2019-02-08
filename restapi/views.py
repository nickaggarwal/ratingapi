from django.http import HttpResponse
from restapi.serializers import ProductSerializer
from restapi.models import Product
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at Leads API.")


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name')
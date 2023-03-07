from rest_framework import generics, viewsets

from .models import *
from .serializers import *


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


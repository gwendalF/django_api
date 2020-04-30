from rest_framework import generics
from api_app.models import Value, Principle
from api_app.serializers import ValueSerializer, PrincipleSerializer


class ValueList(generics.ListAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class ValueDetail(generics.RetrieveAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class PrincipleList(generics.ListAPIView):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer


class PrincipleDetail(generics.RetrieveAPIView):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Value, Principle
from .serializers import ValueSerializer, PrincipleSerializer


class ValueList(APIView):
    def get(self, request):
        values = Value.objects.all()
        data = ValueSerializer(values, many=True).data
        return Response(data)


class ValueDetail(APIView):
    def get(self, request, pk):
        value = get_object_or_404(Value, pk=pk)
        data = ValueSerializer(value).data
        return Response(data)


class PrincipleList(APIView):
    def get(self, request):
        principles = Principle.objects.all()
        data = PrincipleSerializer(principles, many=True).data
        return Response(data)


class PrincipleDetail(APIView):
    def get(self, request, pk):
        principle = get_object_or_404(Principle, pk=pk)
        data = PrincipleSerializer(principle).data
        return Response(data)

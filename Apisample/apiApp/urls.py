from django.urls import path
from .apiviews import ValueList, ValueDetail
from .apiviews import PrincipleList, PrincipleDetail

urlpatterns = [
    path('values/', ValueList.as_view(), name='values_list'),
    path('values/<int:pk>', ValueDetail.as_view(),name='value_detail'),
    path('principles/', PrincipleList.as_view(), name='principles_list'),
    path('principles/<int:pk>/', PrincipleDetail.as_view(), name='principle_detail'),
]
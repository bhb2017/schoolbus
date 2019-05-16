import xadmin
from django.contrib import admin
from django.urls import path
from .views import CarListView,CarDetailView
urlpatterns = [
    path('car_list/', CarListView.as_view(), name='car_list'),
    path('car_detail/<int:car_id>', CarDetailView.as_view(), name='car-detail'),
]
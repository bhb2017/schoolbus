from django.shortcuts import render

from django.views.generic import DetailView, ListView

from car.models import Car,Autoshift

#汽车列表
class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        queryset = super(CarListView, self).get_queryset()
        return queryset.filter(car_state=1)


class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
    


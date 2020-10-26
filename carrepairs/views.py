from django.shortcuts import render
from django.urls import \
    reverse_lazy, \
    reverse

from django.views.generic import \
    CreateView, \
    DeleteView, \
    ListView, \
    UpdateView

from .forms import VehiclesForm

from .models import \
    Vehicles


class VehiclesListView(ListView):
    model = Vehicles
    template_name = 'carrepairs/vehicles_list.html'
    context_object_name = 'vehicle_list'


class VehiclesCreateView(CreateView):
    model = Vehicles
    template_name = 'carrepairs/vehicles_edit.html'
    context_object_name = 'vehicles'
    success_url = reverse_lazy('carrepairs:vehicles_view')
    fields = ['year', 'manufacturer', 'model', 'serial_no']


class VehiclesUpdateView(UpdateView):
    model = Vehicles
    template_name = 'carrepairs/vehicles_edit.html'
    context_object_name = 'vehicles'
    form_class = VehiclesForm
    success_url = reverse_lazy('carrepairs:vehicles_view')


class VehiclesDeleteView(DeleteView):
    model = Vehicles
    template_name = 'carrepairs/vehicles_delete.html'
    context_object_name = 'vehicles'
    success_url = reverse_lazy('carrepairs:vehicles_view')
    form_class = VehiclesForm

    def get_context_data(self, **kwargs):
        context = super(VehiclesDeleteView, self).get_context_data(**kwargs)
        context['action'] = reverse('carrepairs/vehicles_delete',
                                    kwargs={'pk': self.get_object().id})
        return context


from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import LaporanHarian
from .forms import LaporanHarianForm

class LaporanListView(ListView):
    model = LaporanHarian
    template_name = 'laporan/list.html'
    context_object_name = 'items'

class LaporanDetailView(DetailView):
    model = LaporanHarian
    template_name = 'laporan/detail.html'

class LaporanCreateView(CreateView):
    model = LaporanHarian
    form_class = LaporanHarianForm
    template_name = 'laporan/form.html'
    success_url = reverse_lazy('laporan_list')

class LaporanUpdateView(UpdateView):
    model = LaporanHarian
    form_class = LaporanHarianForm
    template_name = 'laporan/form.html'
    success_url = reverse_lazy('laporan_list')

class LaporanDeleteView(DeleteView):
    model = LaporanHarian
    template_name = 'laporan/confirm_delete.html'
    success_url = reverse_lazy('laporan_list')

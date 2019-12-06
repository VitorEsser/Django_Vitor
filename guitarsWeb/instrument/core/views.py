from .models import Instrument, Brand
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView
from .forms import InstrumentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class InstrumentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'register-instrument.html'
    model = Instrument
    form_class = InstrumentForm
    success_url = reverse_lazy('instrument-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querysetBrand = Brand.objects.all()
        context['brands'] = querysetBrand
        return context

    def form_valid(self, form):
        instrument = form.save(commit=False)
        instrument.user = self.request.user
        instrument.save()
        return super().form_valid(form)

class InstrumentListView(LoginRequiredMixin, ListView):
    model = Instrument
    template_name = 'list.html'
    context_object_name = 'instruments'

class MyInstrumentListView(LoginRequiredMixin, ListView):
    model = Instrument
    template_name = 'instrument.html'
    context_object_name = 'instruments'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

class InstrumentDetailView(LoginRequiredMixin, DetailView):
    model = Instrument
    template_name = 'detail-instrument.html'
    context_object_name = 'instruments'

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk'])
        return queryset

class InstrumentUpdateView(LoginRequiredMixin, UpdateView):
    model = Instrument
    template_name = 'edit-instrument.html'
    form_class = InstrumentForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('instrument-list')
    context_object_name = 'instruments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querysetBrand = Brand.objects.all()
        context['brands'] = querysetBrand
        return context

    def form_valid(self, form):
        print('oi')
        instrument = form.save(commit=False)
        instrument.user = self.request.user
        instrument.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
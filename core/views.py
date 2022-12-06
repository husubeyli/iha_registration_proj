from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import IHA
from core.forms import IHACreateForm


class HomePageView(generic.TemplateView):
    template_name = 'base.html'


class IHACreateView(LoginRequiredMixin, generic.CreateView):
    # model = IHA
    form_class = IHACreateForm
    template_name = 'ihas/create.html'
    success_url = reverse_lazy('core:iha_list')


class IHAListView(generic.ListView):
    template_name = 'ihas/list.html'
    model = IHA
    context_object_name = 'ihas'
    paginate_by = 3


class IHADetailView(generic.DetailView):
    template_name = 'ihas/detail.html'
    model = IHA
    slug_field = 'slug'
    context_object_name = 'iha'


class IHADeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'ihas/delete_confirm.html'
    model = IHA
    success_url = reverse_lazy('core:iha_list')


class IHAUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'ihas/update.html'
    form_class = IHACreateForm
    model = IHA
    # success_url = reverse_lazy
    
    def get_success_url(self):
        return reverse('core:iha_detail', kwargs={'slug': self.kwargs['slug']})
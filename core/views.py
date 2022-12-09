from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import IHA
from core.forms import IHACreateForm


class HomePageView(generic.TemplateView):
    template_name = 'base.html'


class IHACreateView(LoginRequiredMixin, generic.CreateView):
    form_class = IHACreateForm
    template_name = 'ihas/create.html'
    success_url = reverse_lazy('core:iha_list')


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
    success_url = reverse_lazy('core:iha_list')


class IHAListView(generic.ListView):
    template_name = 'ihas/list.html'
    model = IHA
    context_object_name = 'ihas_list'
    ordering = '-created_at'
    paginate_by = 1
    # queryset = IHA.objects.all().select_related('markas', 'categories')

    def get_queryset(self):
        queryset = super().get_queryset()
        querydict = self.request.GET
        # get request GET data filter query
        if querydict.get('categories', False):
            queryset = queryset.filter(categories__id__in=list(
                map(int, str(querydict.get('categories')).split('-'))))
        if querydict.get('markas', False):
            queryset = queryset.filter(markas__id__in=list(
                map(int, str(querydict.get('markas')).split('-'))))
        if querydict.get('min_weight', False):
            queryset = queryset.filter(
                weight__gte=int(querydict['min_weight']))
        if querydict.get('max_weight', False):
            queryset = queryset.filter(
                weight__lte=int(querydict['max_weight']))

        # search
        if querydict.get('query', False):
            queryset = queryset.filter(name__icontains=querydict['query'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get datat to template for when pagination changed and page reload data no changed get queryset data
        context["checkbox_categories"] = list(
            map(int, str(self.request.GET.get('categories', 0)).split('-')))
        context["checkbox_markas"] = list(
            map(int, str(self.request.GET.get('markas', 0)).split('-')))
        context["filter_min_weight"] = self.request.GET.get('min_weight', False)
        context["filter_max_weight"] = self.request.GET.get('max_weight', False)
        if self.request.GET.get('query', False):
            context['search_input'] = self.request.GET['query']
        
        return context

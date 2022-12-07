import json
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import IHA
from core.forms import IHACreateForm
from core.tools.checked import is_ajax
from core.models import CategoryIHA, Marka

class HomePageView(generic.TemplateView):
    template_name = 'base.html'


class IHACreateView(LoginRequiredMixin, generic.CreateView):
    # model = IHA
    form_class = IHACreateForm
    template_name = 'ihas/create.html'
    success_url = reverse_lazy('core:iha_list')


# class IHAListView(generic.View):
#     template_name = 'ihas/list.html'
#     # model = IHA
#     # context_object_name = 'ihas'
#     # ordering = '-created_at'
#     # paginate_by = 1
    
    def get(self, request, *args, **kwargs):
        context = {}
        data = {}
        iha_data = IHA.objects.all()
        
        print(request.GET.get("categories"), 'kalam')
        if request.GET.get("categories"):
            print(request.GET.get("categories"),'request.GET.get("categories")')
            
        checkbox_categories = [int(i) for i in request.GET.getlist("categories[]")]  if request.GET.getlist("categories[]") else request.GET.getlist("categories"); # get checked categories and changed type to int
        
        checkbox_markas = [int(i) for i in request.GET.getlist("markas[]")]  if request.GET.getlist("markas[]") else request.GET.getlist("markas"); # get checked markas and changed type to int
        
        checkbox_min_weight = [int(i) for i in request.GET.getlist("min_weight[]")]  if request.GET.getlist("min_weight[]") else request.GET.getlist("min_weight"); # get min weight
        
        checkbox_max_weight = [int(i) for i in request.GET.getlist("max_weight[]")]  if request.GET.getlist("max_weight[]") else request.GET.getlist("max_weight"); # get min weight
        
        context['checkbox_categories_ids'] = checkbox_categories
        context['checkbox_markas_ids'] = checkbox_markas
        context['checkbox_min_weight_ids'] = checkbox_min_weight
        context['checkbox_max_weight_ids'] = checkbox_max_weight
        
        print(checkbox_categories, 'checkbox_categories_ids')
        
        # FILTER PROCCESS
        if is_ajax(request):
            context['checkbox_categories'] = CategoryIHA.objects.filter(id__in=checkbox_categories) if CategoryIHA.objects.filter(id__in=checkbox_categories) else [],
            
            context['checkbox_markas'] = Marka.objects.filter(id__in=checkbox_markas) if Marka.objects.filter(id__in=checkbox_markas) else []
            
            iha_data = iha_data.filter(weight__gte=int(checkbox_min_weight[0]), weight__lte=int(checkbox_max_weight[0]))

            if not checkbox_categories and not checkbox_markas:
                # when unchecked filter return normal data
                context['ihas'] = iha_data
                iha_data = iha_data if iha_data else []
            else:
                if checkbox_categories:
                    iha_data =  iha_data.filter(categories__id__in=checkbox_categories)
                if checkbox_markas:
                    iha_data.filter(markas__id__in=checkbox_markas)
            print(iha_data, 'iha_data')
            # when normal ajax return this pagination
            paginator = Paginator(iha_data, 1) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            context['page_obj'] = page_obj
            context['paginator'] = paginator
            data['include'] = render_to_string(template_name='ihas/filter/filter_data.html',context=context,request=request)
            data['paginate'] = render_to_string(template_name='ihas/filter/pagination.html',context=context,request=request)
            return JsonResponse(data)
        
        iha_data = IHA.objects.all() if IHA.objects.all() else []
    
        # when normal get return this pagination
        paginator = Paginator(iha_data, 1) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        context['paginator'] = paginator
        # context['ihas'] = IHA.objects.all() if IHA.objects.all() else []
        return render(request, self.template_name, context)
    

# class IHAListView(generic.ListView):
#     template_name = 'ihas/list.html'
#     model = IHA
#     context_object_name = 'ihas'
#     ordering = '-created_at'
#     paginate_by = 1
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         data = {}
#         # FILTER PROCCESS
#         checkbox_categories = [int(i) for i in self.request.GET.getlist("categories[]")]  if self.request.GET.getlist("categories[]") else self.request.GET.getlist("categories"); # get checked categories and changed type to int
#         checkbox_markas = [int(i) for i in self.request.GET.getlist("markas[]")]  if self.request.GET.getlist("markas[]") else self.request.GET.getlist("markas"); # get checked markas and changed type to int
        

#         context['checkbox_categories'] = CategoryIHA.objects.filter(id__in=checkbox_categories) if CategoryIHA.objects.filter(id__in=checkbox_categories) else [],
#         context['checkbox_markas'] = Marka.objects.filter(id__in=checkbox_markas) if Marka.objects.filter(id__in=checkbox_markas) else []
        
#         print(checkbox_categories, 'salam')
#         print(checkbox_markas, 'salam')
#         # for filter 
#         if is_ajax(self.request):
#             if not checkbox_categories:
#                 # when unchecked filter return normal data
#                 context['ihas'] = IHA.objects.all().order_by('-created_at')
#                 # data['paginate'] = render_to_string(
#                 #         'category/filter_data.html', context, self.request)
#                 print(type(data), 'baxaqda')
#             else:
#                 context['ihas'] = IHA.objects.filter(categories__id__in=checkbox_categories)
                
#             data['include'] = render_to_string(template_name='ihas/filter/filter_data.html',context=context,request=self.request)
#             return HttpResponse(data, content_type='application/json')
#         context['ihas'] = IHA.objects.all() if IHA.objects.all() else []
#         return context
    



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
    context_object_name = 'ihas'
    ordering = '-created_at'
    paginate_by = 1
    queryset = IHA.objects.all().select_related('markas', 'categories')
    
    def get_queryset(self):
        querydict = self.request.GET
        markas = querydict.get("markas")
        categories = querydict.get("categories")
        qs = super().get_queryset()
        if markas:
            qs.filter(categories__id=categories)
        if categories:
            qs.filter(categories__id=categories)
        return qs
    
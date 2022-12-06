from core import models as core_model




def context_data(request):
    context = {
        'categories': core_model.CategoryIHA.objects.all() if core_model.CategoryIHA.objects.all() else []
    }
    
    return context
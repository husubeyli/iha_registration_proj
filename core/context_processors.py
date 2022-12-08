from core import models as core_model


def context_data(request):
    categories = core_model.CategoryIHA.objects.all()
    markas = core_model.Marka.objects.all()
    max_weight = core_model.IHA.objects.all().order_by('-weight').first()
    min_weight = core_model.IHA.objects.all().order_by('weight').first()
    print(max_weight)
    context = {
        'categories': categories if categories else [],
        'markas': markas if markas else [],
        'max_weight': int(max_weight.weight) + 1 if max_weight != None else 0,
        'min_weight': int(min_weight.weight) if min_weight != None else 0
    }

    return context

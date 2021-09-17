from .models import *


def Categories(request):
    return{
        'categories':P_category.objects.all()
    }





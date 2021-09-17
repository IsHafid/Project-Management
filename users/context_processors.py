from .models import *

def Status(request):
    return{
        'status':Statut.objects.all()
    }





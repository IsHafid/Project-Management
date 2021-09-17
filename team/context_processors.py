from .models import *

def Teams(request):
    return{
        'teams':Team.objects.all()
    }
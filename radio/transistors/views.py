from django.shortcuts import render
from .models import TipTrans

def transistors_all(request):
    tiptrans = TipTrans.objects.all()

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
    }
    return render(request, 'transistors/transistors_list.html', context=context)

# Create your views here.

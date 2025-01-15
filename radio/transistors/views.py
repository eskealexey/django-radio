from django.shortcuts import render
from .models import TipTrans, Transistor

def transistors_all(request):
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.all().order_by('name')

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': transistors,
    }
    return render(request, 'transistors/transistors_list.html', context=context)

# Create your views here.

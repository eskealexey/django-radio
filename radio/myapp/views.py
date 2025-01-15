from django.shortcuts import render

from transistors.models import TipTrans

# Create your views here.
def home(request):
    tiptrans = TipTrans.objects.all()
    context = {
        'title': 'Главная страница',
        'tiptrans': tiptrans,
    }
    return render(request, 'main.html', context=context)

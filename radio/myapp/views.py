from django.shortcuts import render

from .utils import get_context_comm
# Create your views here.
context_comm = get_context_comm()
def home(request):
    context = {
        'title': 'Главная страница',
    }
    context.update(context_comm)
    return render(request, 'main.html', context=context)

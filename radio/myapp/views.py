from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'main.html', context=context)

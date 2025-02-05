from django.core.paginator import Paginator
from django.shortcuts import render

from .models import *
from myapp.utils import get_context_com


# Create your views here.
def moduls_all(request):
    """
    Функция для вывода списка модулей
    """
    # --------------- этот код для поиска по фрагменту наименования транзистора ---------------------------
    if request.method == "GET":
        text = request.GET.get('find')
        if not text or len(text) < 3:
            pass
        else:
            moduls = Modul.objects.filter(name__contains=text).all()
            context = {
                'title': 'Поиск модуля',
                'mods': moduls,
                'tipmod_id': 0,
                'headword': 'Общий список модулей',
            }
            context.update(get_context_com())
            return render(request, 'moduls/modul_list.html', context=context)
    # --------------------------------------------------------------------------------------------------------
    moduls = Modul.objects.all().order_by('name')

    paginator = Paginator(moduls, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Moduls List',
        'mods': page_obj,
        'tipmod_id': 0,
        'headword': 'Общий список модулей',
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_list.html', context=context)


def moduls_tip_list(request, pk):
    """
    Функция для вывода списка модулей по типу
    """
    moduls = Modul.objects.filter(tip_modul_id=pk).order_by('name')

    paginator = Paginator(moduls, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Moduls List',
        'mods': page_obj,
        'tipmod_id': pk,
        'headword': 'Общий список модулей',
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_list.html', context=context)


def moduls_nazn_list(request, nazn_id):
    """
    Функция для вывода списка модулей по назначению
    """
    mods = Modul.objects.filter(naznachenie_id=nazn_id).order_by('name')

    paginator = Paginator(mods, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Moduls List',
        'mods': page_obj,
        'tipmod_id': 0,
        'headword': 'Общий список модулей',
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_list.html', context=context)
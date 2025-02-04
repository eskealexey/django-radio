from django.core.paginator import Paginator
from django.shortcuts import render

from .models import *
from myapp.utils import get_name_korpus, get_context_com


# Create your views here.
def mcu_all(request):
    """
    Функция для вывода списка микроконтроллеров
    """
    # --------------- этот код для поиска по фрагменту наименования транзистора ---------------------------
    if request.method == "GET":
        text = request.GET.get('find')
        if not text or len(text) < 3:
            pass
        else:
            mcus = Mcu.objects.filter(name__contains=text).all()
            if mcus:
                korpus = get_name_korpus(mcus)
            else:
                korpus = ''
            context = {
                'title': 'Поиск МК',
                'mcus': mcus,
                'tipmcu_id': 0,
                'korpus': korpus,
                'headword': 'Общий список МК',
            }
            context.update(get_context_com())
            return render(request, 'mcus/mcu_list.html', context=context)
    # --------------------------------------------------------------------------------------------------------
    mcus = Mcu.objects.all().order_by('name')
    if mcus:
        korpus = get_name_korpus(mcus)
    else:
        korpus = ''

    paginator = Paginator(mcus, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'MCU List',
        'mcus': page_obj,
        'tipmcu_id': 0,
        'korpus': korpus,
        'headword': 'Общий список МК',
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_list.html', context=context)


def mcu_tip_list(request, tipmcu_id):
    """
    Функция для вывода списка MK по типу
    """
    mcus = Mcu.objects.filter(tip_mcu_id=tipmcu_id).order_by('name')
    if mcus:
        korpus = get_name_korpus(mcus)
    else:
        korpus = ''

    paginator = Paginator(mcus, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Mcu List',
        'mcus': page_obj,
        'tipmsu_id': tipmcu_id,
        'korpus': korpus,
        'headword': f'Cписок MK типа "{TipMcu.objects.get(id=tipmcu_id).name}"'
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_list.html', context=context)

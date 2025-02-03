from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Microschema, TipMicroschema, NaznachenieMicroschema, TipKorpusMicroschema
from myapp.utils import get_name_korpus, get_context_com

def microschems_all(request):
    """
    Функция для вывода списка микросхем
    """
# --------------- этот код для поиска по фрагменту наименования транзистора ---------------------------
    if request.method == "GET":
        text = request.GET.get('find')
        if not text or len(text) < 3:
            pass
        else:
            microschems = Microschema.objects.filter(name__contains=text).all()
            if microschems:
                korpus = get_name_korpus(microschems)
            else:
                korpus = ''
            context = {
                'title': 'Поиск микросхемы',
                'microschems': microschems,
                'tipmicro_id': 0,
                'korpus': korpus,
                'headword': 'Общий список микросхем',
            }
            context.update(get_context_com())
            return render(request, 'microschems/microschems_list.html', context=context)
# --------------------------------------------------------------------------------------------------------
    microschems = Microschema.objects.all().order_by('name')
    if microschems:
        korpus = get_name_korpus(microschems)
    else:
        korpus = ''

    paginator = Paginator(microschems, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Microschems List',
        'microschems': page_obj,
        'tipmicro_id': 0,
        'korpus': korpus,
        'headword': 'Общий список микросхем',
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschems_list.html', context=context)


def microschems_tip_list(request, tip_id):
    """
    Функция для вывода списка микросхем по типу
    """
    microschems = Microschema.objects.filter(tip_micro_id=tip_id).order_by('name')
    if microschems:
        korpus = get_name_korpus(microschems)
    else:
        korpus = ''

    paginator = Paginator(microschems, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Microschems List',
        'microschems': page_obj,
        'tipmicro_id': tip_id,
        'korpus': korpus,
        'headword': 'Общий список микросхем',
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschems_list.html', context=context)


def microschems_tip_korpus_list(request,tip_id, korpus_id):
    """
    Функция для вывода списка микросхем по типу и корпусу
    """
    if tip_id == 0:
        microschems = Microschema.objects.filter(tip_korpusa_id=korpus_id).order_by('name')
    else:
        microschems = Microschema.objects.filter(tip_micro_id=tip_id, tip_korpusa_id=korpus_id).order_by('name')

    if microschems:
        korpus = get_name_korpus(microschems)
    else:
        korpus = ''

    paginator = Paginator(microschems, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Microschems List',
        'microschems': page_obj,
        'tipmicro_id': tip_id,
        'korpus': korpus,
        'headword': 'Общий список микросхем',
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschems_list.html', context=context)


def microschems_nazn_list(request, nazn_id):
    """
    Функция для вывода списка микросхем по назначению
    """
    microschems = Microschema.objects.filter(naznachenie_id=nazn_id).order_by('name')
    if microschems:
        korpus = get_name_korpus(microschems)
    else:
        korpus = ''

    paginator = Paginator(microschems, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Microschems List',
        'microschems': page_obj,
        'tipmicro_id': 0,
        'korpus': korpus,
        'headword': 'Общий список микросхем',
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschems_list.html', context=context)
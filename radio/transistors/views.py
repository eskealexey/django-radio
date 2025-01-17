from django.shortcuts import render
from django.core.paginator import Paginator
from .models import TipTrans, Transistor

def get_name_korpus(quary_set:Transistor)->set:
    """
    Функция для получения множества корпусов транзисторов
    """
    korpus = []
    for i in quary_set:
        tuple_ = (i.tip_korpusa.id, i.tip_korpusa.name)
        korpus.append(tuple_)
        setkorpus = set(korpus)
    return setkorpus

def transistors_all(request):
    """
    Функция для вывода списка транзисторов
    """
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.all().order_by('name')
    korpus = get_name_korpus(transistors)

    paginator = Paginator(transistors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': 0,
        'korpus': korpus,
        'headword': 'Общий список транзисторов',
    }
    return render(request, 'transistors/transistors_list.html', context=context)


def transistors_list_tip(request, tiptrans_id):
    """
    Функция для вывода списка транзисторов по типу
    """
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.filter(tip_trans_id=tiptrans_id).order_by('name')
    korpus = get_name_korpus(transistors)

    paginator = Paginator(transistors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': tiptrans_id,
        'korpus': korpus,
        'headword': f'Cписок транзисторов типа "{TipTrans.objects.get(id=tiptrans_id).name}"'
    }
    return render(request, 'transistors/transistors_list.html', context=context)


def transistors_list_tip_korpus(request, tiptrans_id, korpus_id):
    """
    Функция для вывода списка транзисторов по типу и корпусу
    """
    tiptrans = TipTrans.objects.all()

    if tiptrans_id == 0:
        transistors = Transistor.objects.filter(tip_korpusa_id=korpus_id).order_by('name')
    else:
        transistors = Transistor.objects.filter(tip_trans_id=tiptrans_id, tip_korpusa_id=korpus_id).order_by('name')
    korpus = get_name_korpus(transistors)

    paginator = Paginator(transistors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': tiptrans_id,
        'korpus': korpus,
        'headword': f'Cписок транзисторов'    }
    return render(request, 'transistors/transistors_list.html', context=context)


def found_transistors(request, text:str)->None:
    """
    Функция для поиска транзисторов по имени
    """
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.filter(name__icontains=text).order_by('name')
    korpus = get_name_korpus(transistors)

    paginator = Paginator(transistors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': 0,
        'korpus': korpus,
        'headword': f'Поиск транзисторов по имени "{text}"'
    }
    return render(request, 'transistors/transistors_list.html', context=context)
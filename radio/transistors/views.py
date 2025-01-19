from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .admin import DatasheetAdmin
from .forms import TransistorAddForm, DatasheetTransistorAddForm
from .models import TipTrans, Transistor, DatasheetTransistor


def get_name_korpus(quary_)->set:
    """
    Функция для получения множества корпусов транзисторов
    """
    korpus = []
    for i in quary_:
        tuple_ = (i.tip_korpusa.id, i.tip_korpusa.name)
        korpus.append(tuple_)
    return set(korpus)


def transistors_all(request):
    """
    Функция для вывода списка транзисторов
    """
    tiptrans = TipTrans.objects.all()
# --------------- этот код для поиска по фрагменту наименования транзистора ---------------------------
    if request.method == "GET":
        text = request.GET.get('find')
        if not text or len(text) < 3:
            pass
        else:
            transistors = Transistor.objects.filter(name__contains=text).all()
            if transistors:
                korpus = get_name_korpus(transistors)
            else:
                korpus = ''
            context = {
                'tiptrans': tiptrans,
                'title': 'Поиск транзистора',
                'transistors': transistors,
                'tiptrans_id': 0,
                'korpus': korpus,
                'headword': 'Общий список транзисторов',
            }
            return render(request, 'transistors/transistors_list.html', context=context)
# --------------------------------------------------------------------------------------------------------
    transistors = Transistor.objects.all().order_by('name')
    if transistors:
        korpus = get_name_korpus(transistors)
    else:
        korpus = ''

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
    if transistors:
        korpus = get_name_korpus(transistors)
    else:
        korpus = ''

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
    if transistors:
        korpus = get_name_korpus(transistors)
    else:
        korpus = ''

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


def transistor_add(request):
    """
    Функция для добавления нового транзистора
    """
    if request.method == 'POST':
        form = TransistorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transistors_all')
    else:
        form = TransistorAddForm()

    context = {
        'title': 'Добавление нового транзистора',
        'form': form,
    }
    return render(request, 'transistors/transistor_add.html', context=context)


def datasheet_add(request):
    """
    Функция для добавления нового даташита
    """
    if request.method == 'POST':
        form = DatasheetTransistorAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('transistor_add')
    else:
        form = DatasheetTransistorAddForm()
    context = {
        'title': 'Добавление нового транзистора',
        'form': form,
    }
    return render(request, 'transistors/datasheet_transistor_add.html', context=context)

def accounting_(request: HttpRequest, amount: int = 0)-> int:
    """
    Функция для подсчета количества транзисторов
    """
    quantity = request.POST['quantity']
    activ = request.POST['activ']
    print(amount)
    if activ == '+':
        amount += int(quantity)
    else:
        amount -= int(quantity)
        if amount < 0:
            amount = 0
    return amount


def change_transistor_amout(request, transistor_id):
    """
    Функция для изменения количества транзисторов
    """
    if request.method == 'POST':
        transistor = Transistor.objects.get(id=transistor_id)
        amount = transistor.amount
        total = accounting_(request, amount)
        transistor.amount = total
        transistor.save()
        return redirect('transistors_all')
    else:
        return redirect('transistors_all')


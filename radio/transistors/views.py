from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TransistorAddForm, DatasheetTransistorAddForm, TransistorPrimechAddForm, TransistorEditForm
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
    tiptrans = TipTrans.objects.all()
    if request.method == 'POST':
        form = TransistorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transistors_all')
    else:
        form = TransistorAddForm()
    context = {
        'title': 'Добавление нового транзистора',
        'tiptrans': tiptrans,
        'form': form,
    }
    return render(request, 'transistors/transistor_add.html', context=context)


def transistor_edit(request, pk):
    """
    Функция для редактирования транзистора
    """
    tiptrans = TipTrans.objects.all()
    transistor = get_object_or_404(Transistor, id=pk)
    if request.method == 'POST':
        form = TransistorEditForm(request.POST, instance=transistor)
        if form.is_valid():
            form.save()
            return redirect('transistor_detail', pk=pk)
    else:
        form = TransistorEditForm(instance=transistor)
    context = {
        'title': 'Редактирование транзистора',
        'form': form,
        'transistor': transistor,
        'tiptrans': tiptrans,
        'pk': pk,
    }
    return render(request, 'transistors/transistor_edit.html', context=context)


def datasheet_add(request):
    """
    Функция для добавления нового даташита
    """
    tiptrans = TipTrans.objects.all()
    datasheets = DatasheetTransistor.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetTransistorAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/transistors/" + uploaded_file.name
            if DatasheetTransistor.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_trahsisitor_add')
    else:
        form = DatasheetTransistorAddForm()
    context = {
        'title': 'Добавление нового транзистора',
        'tiptrans': tiptrans,
        'datasheets': datasheets,
        'form': form,
    }
    return render(request, 'transistors/datasheet_transistor_add.html', context=context)


def accounting_(request: HttpRequest, amount: int = 0)-> int:
    """
    Функция для подсчета количества транзисторов
    """
    try:
        quantity = int(request.POST.get('quantity', 0))
    except ValueError:
        quantity = 0
    activ = request.POST.get('activ', '+')
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


def transistor_detail(request, pk):
    """
    Функция для вывода детальной информации о транзисторе
    """
    transistor = Transistor.objects.get(id=pk)
    tiptrans = TipTrans.objects.all()
    context = {
        'title': 'Transistor Detail',
        'transistor': transistor,
        'tiptrans': tiptrans,
    }
    return render(request, 'transistors/transistor_detail.html', context=context)


def transistor_primech_change(request, transistor_id):
    """
    Функция для редактирования примечания к транзистору
    """
    transistor = get_object_or_404(Transistor, id=transistor_id)
    context = {
        'title': 'primech',
        'transistor': transistor,
    }
    if request.method == 'POST':
        form = TransistorPrimechAddForm(request.POST, instance=transistor)
        if form.is_valid():
            form.save()
            return redirect('transistor_detail', pk=transistor_id)
    else:
        form = TransistorPrimechAddForm(instance=transistor)
    context['form'] = form
    return render(request, 'transistors/transistor_detail.html', context)


def transistor_count(request, transistor_id):
    """
    Функция для изменения количества транзисторов
    """
    transistor = get_object_or_404(Transistor, id=transistor_id)

    context = {
        'title': 'transistor_count',
        'transistor': transistor,
    }
    if request.method == 'POST':
        amount = transistor.amount
        total = accounting_(request, amount)
        transistor.amount = total
        transistor.save()
        return redirect('transistor_detail', pk=transistor_id)
    else:
        return render(request, 'transistors/transistor_detail.html', context)


def transistor_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления транзистора
    """
    transistor = get_object_or_404(Transistor, id=pk)
    context = {
        'title': 'transistor_removal_confirmation',
        'transistor': transistor,
    }
    return render(request, 'transistors/transistor_removal_confirmation.html', context)


def transistor_delete(request, pk):
    """
    Функция для удаления транзистора
    """
    transistor = get_object_or_404(Transistor, id=pk)
    transistor.delete()
    return redirect('transistors_all')

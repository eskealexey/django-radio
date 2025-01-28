from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TransistorAddForm, DatasheetTransistorAddForm, TransistorPrimechAddForm, TransistorEditForm
from .models import TipTrans, Transistor, DatasheetTransistor
from myapp.utils import get_name_korpus, get_context_comm, accounting_


def transistors_all(request):
    """
    Функция для вывода списка транзисторов
    """
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
                'title': 'Поиск транзистора',
                'transistors': transistors,
                'tiptrans_id': 0,
                'korpus': korpus,
                'headword': 'Общий список транзисторов',
            }
            context.update(get_context_comm())
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
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': 0,
        'korpus': korpus,
        'headword': 'Общий список транзисторов',
    }
    context.update(get_context_comm())
    return render(request, 'transistors/transistors_list.html', context=context)


def transistors_list_tip(request, tiptrans_id):
    """
    Функция для вывода списка транзисторов по типу
    """
    transistors = Transistor.objects.filter(tip_trans_id=tiptrans_id).order_by('name')
    if transistors:
        korpus = get_name_korpus(transistors)
    else:
        korpus = ''

    paginator = Paginator(transistors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': tiptrans_id,
        'korpus': korpus,
        'headword': f'Cписок транзисторов типа "{TipTrans.objects.get(id=tiptrans_id).name}"'
    }
    context.update(get_context_comm())
    return render(request, 'transistors/transistors_list.html', context=context)


def transistors_list_tip_korpus(request, tiptrans_id, korpus_id):
    """
    Функция для вывода списка транзисторов по типу и корпусу
    """
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
        'title': 'Transistors List',
        'transistors': page_obj,
        'tiptrans_id': tiptrans_id,
        'korpus': korpus,
        'headword': f'Cписок транзисторов'    }
    context.update(get_context_comm())
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
    context.update(get_context_comm())
    return render(request, 'transistors/transistor_add.html', context=context)


def transistor_edit(request, pk):
    """
    Функция для редактирования транзистора
    """
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
        'pk': pk,
    }
    context.update(get_context_comm())
    return render(request, 'transistors/transistor_edit.html', context=context)


def datasheet_add(request):
    """
    Функция для добавления нового даташита
    """
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
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_comm())
    return render(request, 'transistors/datasheet_transistor_add.html', context=context)


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
    context = {
        'title': 'Transistor Detail',
        'transistor': transistor,
    }
    context.update(get_context_comm())
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
    context.update(get_context_comm())
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
    context.update(get_context_comm())
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
    context.update(get_context_comm())
    return render(request, 'transistors/transistor_removal_confirmation.html', context)


def transistor_delete(request, pk):
    """
    Функция для удаления транзистора
    """
    transistor = get_object_or_404(Transistor, id=pk)
    transistor.delete()
    return redirect('transistors_all')

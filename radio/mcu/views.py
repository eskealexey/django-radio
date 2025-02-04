from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DatasheetMcuAddForm, McuAddForm, McuEditForm, McuPrimechAddForm
from .models import *
from myapp.utils import get_name_korpus, get_context_com, accounting_


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
        'tipmcu_id': tipmcu_id,
        'korpus': korpus,
        'headword': f'Cписок MK типа "{TipMcu.objects.get(id=tipmcu_id).name}"'
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_list.html', context=context)


def mcu_tip_korpus_list(request, tipmcu_id, korpus_id):
    """
    Функция для вывода списка MK по типу и корпусу
    """
    if tipmcu_id == 0:
        mcus = Mcu.objects.filter(tip_korpusa_id=korpus_id).order_by('name')
    else:
        mcus = Mcu.objects.filter(tip_mcu_id=tipmcu_id, tip_korpusa_id=korpus_id).order_by('name')
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
        'tipmcu_id': tipmcu_id,
        'korpus': korpus,
        'headword': 'Cписок MK'    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_list.html', context=context)


def datasheet_mcu_add(request):
    """
    Функция для добавления нового даташита
    """
    datasheets = DatasheetMcu.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetMcuAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/mcus/" + uploaded_file.name
            if DatasheetMcu.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_mcu_add')
    else:
        form = DatasheetMcuAddForm()
    context = {
        'title': 'Добавление нового MK',
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'mcus/datasheet_mcu_add.html', context=context)


def mcu_add(request):
    """
    Функция для добавления нового MK
    """
    if request.method == 'POST':
        form = McuAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mcu_all')
    else:
        form = McuAddForm()
    context = {
        'title': 'Добавление нового MK',
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_add.html', context=context)


def mcu_detail(request, pk):
    """
    Функция для вывода детальной информации о MK
    """
    mcu = Mcu.objects.get(id=pk)
    context = {
        'title': 'MCU Detail',
        'mcu': mcu,
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_detail.html', context=context)


def mcu_edit(request, pk):
    """
    Функция для редактирования MK
    """
    mcu = get_object_or_404(Mcu, id=pk)
    if request.method == 'POST':
        form = McuEditForm(request.POST, instance=mcu)
        if form.is_valid():
            form.save()
            return redirect('mcu_detail', pk=pk)
    else:
        form = McuEditForm(instance=mcu)
    context = {
        'title': 'Редактирование MK',
        'form': form,
        'mcu': mcu,
        'pk': pk,
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_edit.html', context=context)


def mcu_primech_change(request, pk):
    """
    Функция для редактирования примечания к MK
    """
    mcu = get_object_or_404(Mcu, id=pk)
    context = {
        'title': 'primech',
        'mcu': mcu,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        form = McuPrimechAddForm(request.POST, instance=mcu)
        if form.is_valid():
            form.save()
            return redirect('mcu_detail', pk=pk)
    else:
        form = McuPrimechAddForm(instance=mcu)
    context['form'] = form
    return render(request, 'mcus/mcu_detail.html', context)


def mcu_count(request, pk):
    """
    Функция для изменения количества MK
    """
    mcu = get_object_or_404(Mcu, id=pk)

    context = {
        'title': 'mcu_count',
        'mcu': mcu,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        amount = mcu.amount
        total = accounting_(request, amount)
        mcu.amount = total
        mcu.save()
        return redirect('mcu_detail', pk=pk)
    else:
        return render(request, 'mcus/mcu_detail.html', context)

def mcu_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления MK
    """
    mcu = get_object_or_404(Mcu, id=pk)
    context = {
        'title': 'mcu_removal_confirmation',
        'mcu': mcu,
    }
    context.update(get_context_com())
    return render(request, 'mcus/mcu_removal_confirmation.html', context)


def mcu_delete(request, pk):
    """
    Функция для удаления MK
    """
    mcu = get_object_or_404(Mcu, id=pk)
    mcu.delete()
    return redirect('mcu_all')


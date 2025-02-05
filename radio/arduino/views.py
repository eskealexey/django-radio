from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DatasheetModulAddForm, ModulAddForm, ModulEditForm, ModulPrimechAddForm
from .models import *
from myapp.utils import get_context_com, accounting_


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
        'tipmod_id': nazn_id,
        'headword': 'Общий список модулей',
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_list.html', context=context)


def datasheet_modul_add(request):
    """
    Функция для добавления нового даташита
    """
    datasheets = DatasheetModul.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetModulAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/moduls/" + uploaded_file.name
            if DatasheetModul.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_modul_add')
    else:
        form = DatasheetModulAddForm()
    context = {
        'title': 'Добавление нового модуля',
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'moduls/datasheet_modul_add.html', context=context)


def modul_add(request):
    """
    Функция для добавления нового модуля
    """
    if request.method == 'POST':
        form = ModulAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('moduls_all')
    else:
        form = ModulAddForm()
    context = {
        'title': 'Добавление нового модуля',
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_add.html', context=context)


def modul_edit(request, pk):
    """
    Функция для редактирования модуля
    """
    modul = get_object_or_404(Modul, id=pk)
    if request.method == 'POST':
        form = ModulEditForm(request.POST, instance=modul)
        if form.is_valid():
            form.save()
            return redirect('modul_detail', pk=pk)
    else:
        form = ModulEditForm(instance=modul)
    context = {
        'title': 'Редактирование модуля',
        'form': form,
        'modul': modul,
        'pk': pk,
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_edit.html', context=context)


def modul_detail(request, pk):
    """
    Функция для вывода детальной информации о модуле
    """
    modul = Modul.objects.get(id=pk)
    context = {
        'title': 'Modul Detail',
        'modul': modul,
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_detail.html', context=context)

def modul_primech_change(request, pk):
    """
    Функция для редактирования примечания к модулю
    """
    modul = get_object_or_404(Modul, id=pk)
    context = {
        'title': 'primech',
        'modul': modul,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        form = ModulPrimechAddForm(request.POST, instance=modul)
        if form.is_valid():
            form.save()
            return redirect('modul_detail', pk=pk)
    else:
        form = ModulPrimechAddForm(instance=modul)
    context['form'] = form
    return render(request, 'moduls/modul_detail.html', context)


def modul_count(request, pk):
    """
    Функция для изменения количества модулей
    """
    modul = get_object_or_404(Modul, id=pk)

    context = {
        'title': 'modul_count',
        'modul': modul,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        amount = modul.amount
        total = accounting_(request, amount)
        modul.amount = total
        modul.save()
        return redirect('modul_detail', pk=pk)
    else:
        return render(request, 'moduls/modul_detail.html', context)


def modul_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления модуля
    """
    modul = get_object_or_404(Modul, id=pk)
    context = {
        'title': 'modul_removal_confirmation',
        'modul': modul,
    }
    context.update(get_context_com())
    return render(request, 'moduls/modul_removal_confirmation.html', context)


def modul_delete(request, pk):
    """
    Функция для удаления модуля
    """
    modul = get_object_or_404(Modul, id=pk)
    modul.delete()
    return redirect('moduls_all')


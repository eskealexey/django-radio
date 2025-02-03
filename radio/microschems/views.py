from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DatasheetMicroschemaAddForm, MicroschemaAddForm, MicroschemaEditForm, MicroschemaPrimechAddForm
from .models import Microschema, TipMicroschema, NaznachenieMicroschema, TipKorpusMicroschema, DatasheetMicroschema
from myapp.utils import get_name_korpus, get_context_com, accounting_


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


def datasheet_add(request):
    """
    Функция для добавления нового даташита
    """
    datasheets = DatasheetMicroschema.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetMicroschemaAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/microschems/" + uploaded_file.name
            if DatasheetMicroschema.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_microschema_add')
    else:
        form = DatasheetMicroschemaAddForm()
    context = {
        'title': 'Добавление нового Datasheet',
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'microschems/datasheet_microschema_add.html', context=context)


def microschema_add(request):
    """
    Функция для добавления нновой микросхемы
    """
    if request.method == 'POST':
        form = MicroschemaAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('microschems_all')
    else:
        form = MicroschemaAddForm()
    context = {
        'title': 'Добавление новой микросхемы',
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschema_add.html', context=context)


def microschema_detail(request, pk):
    """
    Функция для вывода детальной информации о микросхеме
    """
    microschema = Microschema.objects.get(id=pk)
    context = {
        'title': 'Microschema Detail',
        'microschema': microschema,
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschema_detail.html', context=context)


def microschema_edit(request, pk):
    """
    Функция для редактирования микросхемы
    """
    microschema = get_object_or_404(Microschema, id=pk)
    if request.method == 'POST':
        form = MicroschemaEditForm(request.POST, instance=microschema)
        if form.is_valid():
            form.save()
            return redirect('microschema_detail', pk=pk)
    else:
        form = MicroschemaEditForm(instance=microschema)
    context = {
        'title': 'Редактирование микросхемы',
        'form': form,
        'microschema': microschema,
        'pk': pk,
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschema_edit.html', context=context)


def microschema_primech_change(request, microschema_id):
    """
    Функция для редактирования примечания к микросхеме
    """
    microschema = get_object_or_404(Microschema, id=microschema_id)
    context = {
        'title': 'primech',
        'microschema': microschema,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        form = MicroschemaPrimechAddForm(request.POST, instance=microschema)
        if form.is_valid():
            form.save()
            return redirect('microschema_detail', pk=microschema_id)
    else:
        form = MicroschemaPrimechAddForm(instance=microschema)
    context['form'] = form
    return render(request, 'microschems/microschema_detail.html', context)


def microschema_count(request, microschema_id):
    """
    Функция для изменения количества транзисторов
    """
    microschema = get_object_or_404(Microschema, id=microschema_id)

    context = {
        'title': 'microschema_count',
        'microschema': microschema,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        amount = microschema.amount
        total = accounting_(request, amount)
        microschema.amount = total
        microschema.save()
        return redirect('microschema_detail', pk=microschema_id)
    else:
        return render(request, 'microschems/microschema_detail.html', context)


def microschema_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления микросхемы
    """
    microschema = get_object_or_404(Microschema, id=pk)
    context = {
        'title': 'microschema_removal_confirmation',
        'microschema': microschema,
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschema_removal_confirmation.html', context)


def microschema_delete(request, pk):
    """
    Функция для удаления микросхемы
    """
    microschema = get_object_or_404(Microschema, id=pk)
    microschema.delete()
    return redirect('microschems_all')

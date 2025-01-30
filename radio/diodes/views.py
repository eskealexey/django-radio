from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from myapp.utils import get_name_korpus, get_context_com, accounting_


from .models import TipDiode, Diode, DatasheetDiode
from .forms import DiodeAddForm, DiodeEditForm, DiodePrimechAddForm, DatasheetDiodeAddForm


class DiodeListView(ListView):
    """
    Класс для вывода списка диодов
    """
    model = Diode
    template_name = 'diodes/diodes_list.html'
    context_object_name = 'diodes'
    paginate_by = 25  # Количество элементов на странице

    def get_queryset(self):
        """
        Переопределение метода get_queryset для фильтрации диодов по запросу
        """
        queryset = super().get_queryset().order_by('name')
        text = self.request.GET.get('find')

        if text and len(text) >= 3:
            queryset = queryset.filter(name__contains=text)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Переопределение метода для добавления необходимых данных в контекст
        """
        context = super().get_context_data(**kwargs)
        context.update(get_context_com())
        context['tipdiode_id'] = 0
        context['headword'] = 'Общий список диодов'
        context['title'] = 'Diodes List'
        # Получаем корпус для текущего запроса
        diodes = self.get_queryset()
        context['korpusa_diode'] = get_name_korpus(diodes) if diodes else ''

        return context


class DiodeListTipView(ListView):
    """
    Класс для вывода списка диодов по типу
    """
    model = Diode
    template_name = 'diodes/diodes_list.html'
    context_object_name = 'diodes'
    paginate_by = 25

    def get_queryset(self):
        tipdiode_id = self.kwargs['tipdiode_id']
        diodes = Diode.objects.filter(tip_diode_id=tipdiode_id).order_by('name')
        if diodes:
            korpus = get_name_korpus(diodes)
        else:
            korpus = ''
        return diodes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_com())
        context['title'] = 'Diodes List'
        context['tipdiode_id'] = self.kwargs['tipdiode_id']
        context['korpusa_diode'] = get_name_korpus(self.get_queryset())
        context['headword'] = f'Cписок диодов типа "{TipDiode.objects.get(id=self.kwargs["tipdiode_id"]).name}"'
        return context


class DiodeListTipKorpusView(ListView):
    """
    Класс для вывода списка диодов по типу и корпусу
    """
    model = Diode
    template_name = 'diodes/diodes_list.html'
    context_object_name = 'diodes'
    paginate_by = 25

    def get_queryset(self):
        tip_id = self.kwargs['tip_id']
        korpus_id = self.kwargs['korpus_id']
        if tip_id == 0:
            diodes = Diode.objects.filter(tip_korpusa_id=korpus_id).order_by('name')
        else:
            diodes = Diode.objects.filter(tip_diode_id=tip_id, tip_korpusa_id=korpus_id).order_by('name')
        if diodes:
            korpus = get_name_korpus(diodes)
        else:
            korpus = ''
        return diodes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_context_com())
        context['title'] = 'Diodes List'
        context['tipdiode_id'] = self.kwargs['tip_id']
        context['korpusa_diode'] = get_name_korpus(self.get_queryset())
        context['headword'] = f'Cписок диодов'
        return context


class DiodeAddView(CreateView):
    """
    Класс для добавления нового диода
    """
    model = Diode
    form_class = DiodeAddForm
    template_name = 'diodes/diode_add.html'
    success_url = '/diodes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление нового диода'
        context.update(get_context_com())
        return context


class DiodeDetailView(DetailView):
    """
    Класс для вывода детальной информации о диоде
    """
    model = Diode
    template_name = 'diodes/diode_detail.html'
    context_object_name = 'diode'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Diode Detail'
        context.update(get_context_com())
        return context


class DiodeEditView(UpdateView):
    """
    Класс для редактирования диода
    """
    model = Diode
    form_class = DiodeEditForm
    template_name = 'diodes/diode_edit.html'
    context_object_name = 'diode'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование диода'
        context.update(get_context_com())
        return context

    def get_success_url(self):
        return reverse('diode_detail', kwargs={'pk': self.object.pk})


class DiodePrimechChangeView(UpdateView):
    """
    Класс для редактирования примечания к диоду
    """
    model = Diode
    form_class = DiodePrimechAddForm
    template_name = 'diodes/diodes_detail.html'
    context_object_name = 'diode'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'primech'
        context.update(get_context_com())
        return context

    def get_success_url(self):
        return reverse('diode_detail', kwargs={'pk': self.object.pk})


def datasheet_diode_add(request):
    """
    Функция для добавления нового даташита
    """
    datasheets = DatasheetDiode.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetDiodeAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/diodes/" + uploaded_file.name
            if DatasheetDiode.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_diode_add')
    else:
        form = DatasheetDiodeAddForm()
    context = {
        'title': 'Добавление нового даташита диода',
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'diodes/datasheet_diode_add.html', context=context)


def change_diode_amout(request, pk):
    """
    Функция для изменения количества транзисторов
    """
    if request.method == 'POST':
        diode = Diode.objects.get(id=pk)
        amount = diode.amount
        total = accounting_(request, amount)
        diode.amount = total
        diode.save()
        return redirect('diodes_all')
    else:
        return redirect('diodes_all')


def diode_count(request, pk):
    """
    Функция для изменения количества диодов
    """
    diode = get_object_or_404(Diode, id=pk)

    context = {
        'title': 'diode_count',
        'diode': diode,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        amount = diode.amount
        total = accounting_(request, amount)
        diode.amount = total
        diode.save()
        return redirect('diode_detail', pk=pk)
    else:
        return render(request, 'diodes/diode_detail.html', context)


def diode_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления диода
    """
    diode = get_object_or_404(Diode, id=pk)
    context = {
        'title': 'diode_removal_confirmation',
        'diode': diode,
    }
    context.update(get_context_com())
    return render(request, 'diodes/diode_removal_confirmation.html', context)


def diode_delete(request, pk):
    """
    Функция для удаления транзистора
    """
    diode = get_object_or_404(Diode, id=pk)
    diode.delete()
    return redirect('diodes_all')

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from myapp.utils import get_context_com, get_name_korpus, accounting_

from .forms import StabilizerAddForm, StabilizerPrimechAddForm, DatasheetStabilizerAddForm, StabilizerEditForm
from .models import Stabilizer, TipStabilizer, DatasheetStabilizer


# Create your views here.

class StabilizersListView(ListView):
    """
    Класс для вывода списка стабилизаторов
    """
    model = Stabilizer
    template_name = 'stabilizers/stabilizers_list.html'
    context_object_name = 'stabilizers'
    paginate_by = 25  # Количество элементов на странице

    def get_queryset(self):
        """
        Переопределение метода get_queryset для фильтрации стабилизаторов по запросу
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
        context['tipstab_id'] = 0
        context['headword'] = 'Общий список стабилизаторов'
        context['title'] = 'Stabilizers List'
        # Получаем корпус для текущего запроса
        stabilizers = self.get_queryset()
        context['korpusa_stab'] = get_name_korpus(stabilizers) if stabilizers else ''
        return context


class StabilizersListTipView(ListView):
    """
    Класс для вывода списка диодов по типу
    """
    model = Stabilizer
    template_name = 'stabilizers/stabilizers_list.html'
    context_object_name = 'stabilizers'
    paginate_by = 25

    def get_queryset(self):
        """
        Переопределение метода get_queryset для фильтрации стабилизаторов по типу
        """
        tipstab_id = self.kwargs['tipstab_id']
        stabilizers = Stabilizer.objects.filter(tip_stab_id=tipstab_id).order_by('name')
        if stabilizers:
            korpus = get_name_korpus(stabilizers)
        else:
            korpus = ''
        return stabilizers

    def get_context_data(self, **kwargs):
        """
        Переопределение метода для добавления необходимых данных в контекст
        """
        context = super().get_context_data(**kwargs)
        context.update(get_context_com())
        context['title'] = 'Stabilizers List'
        context['tipstab_id'] = self.kwargs['tipstab_id']
        context['korpusa_stab'] = get_name_korpus(self.get_queryset())
        context['headword'] = f'Cписок стабилизаторов типа "{TipStabilizer.objects.get(id=self.kwargs["tipstab_id"]).name}"'
        return context


class StabilizersListTipKorpusView(ListView):
    """
    Класс для вывода списка стабилизаторов по типу и корпусу
    """
    model = Stabilizer
    template_name = 'stabilizers/stabilizers_list.html'
    context_object_name = 'stabilizers'
    paginate_by = 25

    def get_queryset(self):
        """
        Переопределение метода get_queryset для фильтрации стабилизаторов по типу и корпусу
        """
        tipstab_id = self.kwargs['tipstab_id']
        korpus_id = self.kwargs['korpus_id']
        if tipstab_id == 0:
            stabilizirs = Stabilizer.objects.filter(tip_korpusa=korpus_id).order_by('name')
        else:
            stabilizirs = Stabilizer.objects.filter(tip_stab_id=tipstab_id, tip_korpusa_id=korpus_id).order_by('name')
        if stabilizirs.exists():
            korpus = get_name_korpus(stabilizirs)
        else:
            korpus = ''
        return stabilizirs

    def get_context_data(self, **kwargs):
        """
        Переопределение метода для добавления необходимых данных в контекст
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stabilizers List'
        context['tipstab_id'] = self.kwargs['tipstab_id']
        context['korpusa_stab'] = get_name_korpus(self.get_queryset())
        context['headword'] = 'Список стабилизаторов'
        context.update(get_context_com())
        return context


class StabilizerAddView(CreateView):
    """
    Класс для добавления нового стабилизатора
    """
    model = Stabilizer
    form_class = StabilizerAddForm
    template_name = 'stabilizers/stabilizer_add.html'
    success_url = '/stab/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление нового стабилизатора'
        context.update(get_context_com())
        return context


class StabilizerEditView(UpdateView):
    """
    Класс для редактирования диода
    """
    model = Stabilizer
    form_class = StabilizerEditForm
    template_name = 'stabilizers/stabilizer_edit.html'
    context_object_name = 'stabilizer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование диода'
        context.update(get_context_com())
        return context

    def get_success_url(self):
        return reverse('stabilizer_detail', kwargs={'pk': self.object.pk})


class StabilizerDetailView(DetailView):
    """
    Класс для вывода детальной информации о диоде
    """
    model = Stabilizer
    template_name = 'stabilizers/stabilizer_detail.html'
    context_object_name = 'stabilizer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stabilizer Detail'
        context.update(get_context_com())
        return context


class StabilizerPrimechChangeView(UpdateView):
    """
    Класс для редактирования примчания
    """
    model = Stabilizer
    form_class = StabilizerPrimechAddForm
    template_name = 'stabilizers/stabilizer_detail.html'
    context_object_name = 'stabilizer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'primech'
        context.update(get_context_com())
        return context

    def get_success_url(self):
        return reverse('stabilizer_detail', kwargs={'pk': self.object.pk})


def change_stabilizer_amout(request, pk):
    """
    Функция для изменения количества стабилизаторов
    """
    if request.method == 'POST':
        stabilizer = Stabilizer.objects.get(id=pk)
        amount = stabilizer.amount
        total = accounting_(request, amount)
        stabilizer.amount = total
        stabilizer.save()
        return redirect('stabilisers_all')
    else:
        return redirect('stabilisers_all')


def stabilizer_count(request, pk):
    """
    Функция для изменения количества диодов
    """
    stabilizer = get_object_or_404(Stabilizer, id=pk)

    context = {
        'title': 'stabilizer_count',
        'stabilizer': stabilizer,
    }
    context.update(get_context_com())
    if request.method == 'POST':
        amount = stabilizer.amount
        total = accounting_(request, amount)
        stabilizer.amount = total
        stabilizer.save()
        return redirect('stabilizer_detail', pk=pk)
    else:
        return render(request, 'stabilizers/stabilizer_detail.html', context)


def datasheet_stabilizer_add(request):
    """
    Функция для добавления нового даташита
    """
    datasheets = DatasheetStabilizer.objects.all().order_by('discription')
    if request.method == 'POST':
        form = DatasheetStabilizerAddForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['url']
            file = "datasheets/stabilizers/" + uploaded_file.name
            if DatasheetStabilizer.objects.filter(url=file).exists():
                messages.error(request, f"Файл с именем <b>{uploaded_file.name}</b> уже существует.")
            else:
                messages.success(request, f"Файл <b>{uploaded_file.name}</b> успешно загружен.")
                form.save()
            return redirect('datasheet_stabilizer_add')
    else:
        form = DatasheetStabilizerAddForm()
    context = {
        'title': 'Добавление нового даташита стабилизатора',
        'datasheets': datasheets,
        'form': form,
    }
    context.update(get_context_com())
    return render(request, 'stabilizers/datasheet_stabilizer_add.html', context=context)


def stabilizer_removal_confirmation(request, pk):
    """
    Функция для подтверждения удаления стабилизатора
    """
    stabilizer = get_object_or_404(Stabilizer, id=pk)
    context = {
        'title': 'stabilizer_removal_confirmation',
        'stabilizer': stabilizer,
    }
    context.update(get_context_com())
    return render(request, 'stabilizers/stabilizer_removal_confirmation.html', context)


def stabilizer_delete(request, pk):
    """
    Функция для удаления стабилизатора
    """
    stabilizer = get_object_or_404(Stabilizer, id=pk)
    stabilizer.delete()
    return redirect('stabilisers_all')
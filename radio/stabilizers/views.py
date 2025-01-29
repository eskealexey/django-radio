from django.views.generic import ListView, CreateView, DetailView
from myapp.utils import get_context_com, get_name_korpus

from .forms import StabilizerAddForm
from .models import Stabilizer, TipStabilizer


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
    Класс для добавления нового диода
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
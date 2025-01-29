from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from myapp.utils import get_context_com, get_name_korpus
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
        print(context['tipstabs'])
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


def stabilizirs_list_tip_korpus(request, tipstab_id, korpus_id):
    """
    Функция для вывода списка транзисторов по типу и корпусу
    """
    if tipstab_id == 0:
        stabilizirs = Stabilizer.objects.filter(tip_korpusa_id=korpus_id).order_by('name')
    else:
        stabilizirs = Stabilizer.objects.filter(tip_stab_id=tipstab_id, tip_korpusa_id=korpus_id).order_by('name')
    if stabilizirs:
        korpus = get_name_korpus(stabilizirs)
    else:
        korpus = ''

    paginator = Paginator(stabilizirs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Stabiliziers List',
        'stabilizirs': page_obj,
        'tipstabs_id': tipstab_id,
        'korpus': korpus,
        'headword': f'Cписок стабилизаторв'    }
    context.update(get_context_com())
    return render(request, 'stabilizers/stabilizers_list.html', context=context)


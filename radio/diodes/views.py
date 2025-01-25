from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from .models import TipDiode, TipKorpusDiode, DatasheetDiode, Diode
from myapp.utils import get_name_korpus


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
        context['tip_diode'] = TipDiode.objects.all()
        context['tipdiode_id'] = 0
        context['headword'] = 'Общий список диодов'
        context['title'] = 'Diodes List'
        # Получаем корпус для текущего запроса
        diodes = self.get_queryset()
        context['korpusa_diode'] = get_name_korpus(diodes) if diodes else ''

        return context


class DiodesListView(ListView):
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
        context['tip_diode'] = TipDiode.objects.all()
        context['title'] = 'Diodes List'
        context['tipdiode_id'] = self.kwargs['tipdiode_id']
        context['korpusa_diode'] = get_name_korpus(self.get_queryset())
        context['headword'] = f'Cписок диодов типа "{TipDiode.objects.get(id=self.kwargs["tipdiode_id"]).name}"'
        return context

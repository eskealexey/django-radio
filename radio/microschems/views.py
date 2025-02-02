from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Microschema, TipMicroschema, NaznachenieMicroschema, TipKorpusMicroschema
from myapp.utils import get_name_korpus, get_context_com



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
                'naznach': NaznachenieMicroschema.objects.all(),
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
        'naznach': NaznachenieMicroschema.objects.all(),
        'korpus': korpus,
        'headword': 'Общий список микросхем',
    }
    context.update(get_context_com())
    return render(request, 'microschems/microschems_list.html', context=context)
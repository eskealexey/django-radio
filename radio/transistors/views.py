from django.shortcuts import render
from django.core.paginator import Paginator
from .models import TipTrans, Transistor

def transistors_all(request):
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.all().order_by('name')

    paginator = Paginator(transistors, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': page_obj,
        'headword': 'Общий список транзисторов',
    }
    return render(request, 'transistors/transistors_list.html', context=context)


def transistors_list_tip(request, tiptrans_id):
    tiptrans = TipTrans.objects.all()
    transistors = Transistor.objects.filter(tip_trans_id=tiptrans_id).order_by('name')

    context = {
        'tiptrans': tiptrans,
        'title': 'Transistors List',
        'transistors': transistors,
        'headword': f'Cписок транзисторов типа "{TipTrans.objects.get(id=tiptrans_id).name}"'
    }
    return render(request, 'transistors/transistors_list.html', context=context)

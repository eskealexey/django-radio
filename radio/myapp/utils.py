from django.http import HttpRequest
from transistors.models import TipTrans
from diodes.models import TipDiode
from stabilizers.models import TipStabilizer
from microschems.models import TipMicroschema, NaznachenieMicroschema


def get_name_korpus(quary_)->set:
    """
    Функция для получения множества корпусов транзисторов
    """
    korpus = []
    for i in quary_:
        tuple_ = (i.tip_korpusa.id, i.tip_korpusa.name)
        korpus.append(tuple_)
    return set(korpus)


def get_context_com()-> dict:
    """
    Функция для получения контекста для общего меню
    """
    tiptrans = TipTrans.objects.all()
    tipdiodes = TipDiode.objects.all()
    tipstabs = TipStabilizer.objects.all()
    tipmicroschems = TipMicroschema.objects.all()
    naznach = NaznachenieMicroschema.objects.all()
    context = {
        'tiptrans': tiptrans,
        'tip_diode': tipdiodes,
        'tipstabs': tipstabs,
        'tipmicroschems': tipmicroschems,
        'naznach': naznach,
    }
    return context


def accounting_(request: HttpRequest, amount: int = 0)-> int:
    """
    Функция для подсчета количества транзисторов
    """
    try:
        quantity = int(request.POST.get('quantity', 0))
    except ValueError:
        quantity = 0
    activ = request.POST.get('activ', '+')
    if activ == '+':
        amount += int(quantity)
    else:
        amount -= int(quantity)
        if amount < 0:
            amount = 0
    return amount

from transistors.models import TipTrans
from diodes.models import TipDiode


def get_name_korpus(quary_)->set:
    """
    Функция для получения множества корпусов транзисторов
    """
    korpus = []
    for i in quary_:
        tuple_ = (i.tip_korpusa.id, i.tip_korpusa.name)
        korpus.append(tuple_)
    return set(korpus)


def get_context_comm()->dict:
    """
    Функция для получения контекста меню
    """
    context_comm = {
        'tiptrans': TipTrans.objects.all(),
        'tip_diode': TipDiode.objects.all(),
    }

    return context_comm
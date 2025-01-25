def get_name_korpus(quary_)->set:
    """
    Функция для получения множества корпусов транзисторов
    """
    korpus = []
    for i in quary_:
        tuple_ = (i.tip_korpusa.id, i.tip_korpusa.name)
        korpus.append(tuple_)
    return set(korpus)
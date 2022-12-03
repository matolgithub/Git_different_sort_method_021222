from random import shuffle
import datetime


def choice_sort_func():
    """
    Общий смысл сортировки - деление списка на две части: отсортированную и неотсорторованную. 1. Проверяется список,
    находится мин значение. Заносится в сорт часть. 2. Индекс нач элемента несорт списка увеличивается на 1. Далее
    опять п.1. И так, пока нач индекс не станет равным последнему индексу списка.
    """
    # формируем рандомный список
    list_for_choice_sorting = [item for item in range(10000)]
    shuffle(list_for_choice_sorting)
    print(list_for_choice_sorting)

    # начальный и последний индексы списка
    first_index = 0
    last_index = len(list_for_choice_sorting) - 1

    start = datetime.datetime.now()

    while first_index <= last_index:
        # в цикле проверяем и находим минимальное значение
        min_value = min(list_for_choice_sorting[first_index:])

        # помещаем это мин значение в начало списка
        index_min_value = list_for_choice_sorting.index(min_value)
        list_for_choice_sorting[first_index], list_for_choice_sorting[index_min_value] = \
            list_for_choice_sorting[index_min_value], list_for_choice_sorting[first_index]

        # увеличиваем индекс первого элемента на 1
        first_index += 1

    print(list_for_choice_sorting)
    print(f"Total time: {datetime.datetime.now() - start}. It is 6 times quickest then bubble sorting method!")

    return list_for_choice_sorting


if __name__ == "__main__":
    choice_sort_func()

from random import shuffle
import datetime


def insert_sort_func():
    # формируем рандомный список
    list_for_insert_sorting = [item for item in range(20000)]
    shuffle(list_for_insert_sorting)
    print(list_for_insert_sorting)

    # начальный и последний индексы списка
    first_sort_index = 0
    new_sorting_list = []

    start = datetime.datetime.now()

    while list_for_insert_sorting != []:
        unsort_value = list_for_insert_sorting.pop(first_sort_index)
        if new_sorting_list == []:
            new_sorting_list.append(unsort_value)
        else:
            for sort_value in new_sorting_list:
                if unsort_value < sort_value:
                    new_sorting_list.insert(new_sorting_list.index(sort_value), unsort_value)
                    break
                elif unsort_value > new_sorting_list[-1]:
                    new_sorting_list.append(unsort_value)
                    break

    print(new_sorting_list)
    # 10000 - 1,77 sec - like choice sorting, 20000 - 6,85sec some quickest aither choice sorting!
    print(datetime.datetime.now() - start)


if __name__ == "__main__":
    insert_sort_func()

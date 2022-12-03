from random import shuffle


def choice_sort_func():
    list_for_choice_sorting = [item for item in range(10)]
    shuffle(list_for_choice_sorting)
    print(list_for_choice_sorting)


if __name__ == "__main__":
    choice_sort_func()

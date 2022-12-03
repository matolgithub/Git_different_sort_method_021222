import datetime


def bubble_sort(list_items):
    start_time = datetime.datetime.now()

    last_index = len(list_items) - 1

    while last_index >= 0:
        first_index = 0
        while first_index <= last_index - 1:
            second_index = first_index + 1
            if list_items[first_index] > list_items[second_index]:
                list_items[first_index], list_items[second_index] = list_items[second_index], list_items[first_index]
            first_index += 1
        last_index -= 1

    total_time = datetime.datetime.now() - start_time

    return list_items


if __name__ == "__main__":
    print(bubble_sort([4, 2, 3, 1]))

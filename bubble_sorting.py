import random
import datetime
from random import shuffle

list_items = [item for item in range(5)]
shuffle(list_items)
print(f"The random_start_list: \n{list_items}.")

new_sorting_list = []
start_time = datetime.datetime.now()
while list_items != []:
    first_index = 0
    second_index = first_index + 1
    while first_index <= (len(list_items) - 2):
        if list_items[first_index] < list_items[second_index]:
            first_index += 1
            continue
        else:
            list_items[first_index], list_items[second_index] = list_items[second_index], list_items[first_index]
        first_index += 1
    new_sorting_list.append(list_items[-1])
    list_items = list_items[:-1]
# new_sorting_list = new_sorting_list[::-1]
print(f"New sorting list: \n{new_sorting_list}")

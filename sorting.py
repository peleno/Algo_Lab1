from random import randint
from typing import List
from farm import Farm

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def selection_sort_by_power_desc(array: List[Farm]):
    number_of_comparisons = 0
    number_of_swaps = 0
    length = len(array)
    for i in range(length - 1):
        max_elem_index = i
        for j in range(i + 1, length):
            number_of_comparisons += 1
            if array[j].power > array[max_elem_index].power:
                max_elem_index = j

        temp = array[max_elem_index]
        array[max_elem_index] = array[i]
        array[i] = temp
        number_of_swaps += 1
    return number_of_comparisons, number_of_swaps

def partition3(array: List[Farm], left, right):
    number_of_swaps = 0
    number_of_comparisons = 0
    pivot = array[left].animals_count
    leftmost_pivot_index = left
    rightmost_pivot_index = right
    i = left
    while i <= rightmost_pivot_index:

        number_of_comparisons += 1
        if array[i].animals_count < pivot:
            number_of_swaps += 1
            swap(array, leftmost_pivot_index, i)
            leftmost_pivot_index += 1
            i += 1
        elif array[i].animals_count > pivot:
            number_of_swaps += 1
            swap(array, i, rightmost_pivot_index)
            rightmost_pivot_index -= 1
        else:
            i += 1
    return leftmost_pivot_index, rightmost_pivot_index, number_of_comparisons, number_of_swaps

def quick_sort_by_animals_count_asc(array: List[Farm], left, right):
    if left >= right:
        return 0, 0

    rand_pivot_index = randint(left, right)
    swap(array, left, rand_pivot_index)
    leftmost_pivot, rightmost_pivot, comparisons, swaps = partition3(array, left, right)
    left_result = quick_sort_by_animals_count_asc(array, left, leftmost_pivot - 1)
    right_result = quick_sort_by_animals_count_asc(array, rightmost_pivot + 1, right)

    number_of_comparisons = comparisons + left_result[0] + right_result[1]
    number_of_swaps = swaps + left_result[1] + right_result[1]
    return number_of_comparisons, number_of_swaps

import time
from farm import Farm
from sorting import selection_sort_by_power_desc
from sorting import quick_sort_by_animals_count_asc
from csv import DictReader


farms = []
with open('farms_small.csv') as f:
    reader = DictReader(f)
    for row in reader:
        farms.append(Farm(row['location'], row['animals_count'], row['power']))

print('***************** Selection sort **********************')
selection_start = time.time()
number_of_comparisons, number_of_swaps = selection_sort_by_power_desc(farms)
selection_end = time.time()

print('Number of comparisons:', number_of_comparisons)
print('Number of swaps:', number_of_swaps)
print('Time:', selection_end - selection_start)
print('Farms sorted by power, descending:')
for farm in farms:
    print(farm)


print()
print('**************** Quick sort ***********************')
quick_sort_start = time.time()
number_of_comparisons, number_of_swaps = quick_sort_by_animals_count_asc(farms, 0, len(farms) - 1)
quick_sort_end = time.time()

print('Number of comparisons:', number_of_comparisons)
print('Number of swaps:', number_of_swaps)
print('Time:', quick_sort_end - quick_sort_start)
print('Farms sorted by animals count, ascending:')
for farm in farms:
    print(farm)


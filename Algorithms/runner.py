from comparison_sorts import *
import random

if __name__ == '__main__':
    # lst = [1, 2, 5, 6, 0, 3, 6, 4, 10, -9]
    lst = [*range(-12, 12)]
    random.shuffle(lst)
    print('Intitially:', lst)
    print('-'*120, '+', sep='')
    print('Algorithm\t|\t\t\t\t\t\t\tOutput\t\t\t\t\t\t|')
    print('-'*120, '+', sep='')
    print('Selection sort\t|\t', selection(lst.copy()), '\t|')
    print('Bubble sort\t|\t', bubble(lst.copy()), '\t|')
    print('Insertion sort\t|\t', insertion(lst.copy()), '\t|')
    print('Shell sort\t|\t', shellsort(lst.copy()), '\t|')
    print('Exchange sort\t|\t', exchange_sort(lst.copy()), '\t|')
    print('Gnome sort\t|\t', gnome_sort(lst.copy()), '\t|')
    print('Even-odd sort\t|\t', even_odd(lst.copy()), '\t|')
    print('Heap sort\t|\t', heapsort(lst.copy()), '\t|')
    print('Merge sort\t|\t', merge_sort(lst.copy()), '\t|')
    print('Quick sort\t|\t', quicksort(lst.copy()), '\t|')
    print('-'*120, '+', sep='')

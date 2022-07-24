############################################ Selection Sort ############################################
def selection(lst):
    for i in range(len(lst)):
        mini = i
        for j in range(i, len(lst)):
            if lst[j] < lst[mini]:
                mini = j
        lst[i], lst[mini] = lst[mini], lst[i]
    return lst

############################################ Bubble Sort ############################################
def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

############################################ Insertion Sort ############################################
def insertion(lst, k=1):
    for i in range(1, len(lst)):
        while i > 0 and lst[i-k] > lst[i]:
            lst[i-k], lst[i] = lst[i], lst[i-k]
            i -= 1
    return lst

############################################ Shell sort ############################################
def shellsort(lst):
    '''
    Variation of insertion sort
    '''
    n = len(lst)
    # Sort an array a[0...n-1].
    # gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # Ciura gap sequence
    gaps = [i// 2 for i in range(n, 0, -n//2+1)]

    # Start with the largest gap and work down to a gap of 1
    # similar to insertion sort but instead of 1, gap is being used in each step
    for gap in gaps:
        # Do a gapped insertion sort for every elements in gaps
        # Each loop leaves a[0..gap-1] in gapped order
        lst = insertion(lst, gap)
    return lst

############################################ Exchange Sort ############################################
def exchange_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

############################################ Gnome Sort ############################################
def gnome_sort(lst):
    i = 0
    while i < len(lst):
        if i == 0 or lst[i] >= lst[i-1]:
            i += 1
        else:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
    return lst

############################################ Even-odd Sort ############################################
def even_odd(lst):
    even_range, odd_range = range(0, len(lst)-1, 2), range(1, len(lst)-1, 2)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in even_range:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
        for i in odd_range:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
    return lst

############################################ Heap Sort ############################################
def max_heapify(heap, heap_size, parent):
    left = 2*parent
    right = 2*parent + 1
    largest = parent
    if left < heap_size and heap[left] > heap[largest]:
        largest = left
    if right < heap_size and heap[right] > heap[largest]:
        largest = right
    if largest != parent:
        heap[parent], heap[largest] = heap[largest], heap[parent]
        max_heapify(heap, heap_size, largest)

def build_max_heap(lst):
    heap_size = len(lst)

    for i in range (heap_size//2, -1, -1):
        max_heapify(lst,heap_size, i)
    return lst  # lst is a heap representation now

def heapsort(lst):
    heap_size = len(lst)
    heap = build_max_heap(lst)
    for i in range(heap_size-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heap_size -= 1
        max_heapify(heap, heap_size, 0)
    return heap # which is a sorted representation of lst now

############################################ Merge Sort ############################################
def partition(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        return merge(partition(lst[:mid]), partition(lst[mid:]))
    return lst

merge_sort = partition

def merge(lst1, lst2):
    res = []
    l, r = 0, 0
    while l < len(lst1) and r < len(lst2):
        if lst1[l] <= lst2[r]:
            res.append(lst1[l])
            l += 1
        else:
            res.append(lst2[r])
            r += 1
    res.extend(lst1[l:])
    res.extend(lst2[r:])
    return res

############################################ Quicksort ############################################
import random
def quicksort(lst):
    if len(lst) > 1:
        pivot = random.choice(lst)
        return quicksort([x for x in lst if x < pivot]) + [x for x in lst if x == pivot] + quicksort([x for x in lst if x > pivot])
    return lst

############################################ Introsort ############################################

############################################ Timsort ############################################

############################################ Block Sort ############################################

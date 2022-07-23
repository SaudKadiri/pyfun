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
        pivot = lst[random.randrange(len(lst))]
        return quicksort([*filter(lambda x: x < pivot, lst)]) + [pivot] * lst.count(pivot) + quicksort([*filter(lambda x: x > pivot, lst)])
    return lst

############################################ Shellsort ############################################
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

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if __name__ == '__main__':
    lst = [1, 2, 5, 6, 0, 3, 6, 4, 10, -9]

    print('Bubble sort\t', bubble(lst.copy()))
    print('Insertion sort\t', insertion(lst.copy()))
    print('Merge sort\t', merge_sort(lst.copy()))
    print('Quicksort\t', quicksort(lst.copy()))
    print('Shellsort\t', shellsort(lst.copy()))

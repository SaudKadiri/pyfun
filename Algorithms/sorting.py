import random

############################################ Bubble Sort ############################################
def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

############################################ Insertion Sort ############################################
def insertion(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j -= 1
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
def quicksort(lst):
    if len(lst) > 1:
        pivot = lst[random.randrange(len(lst))]
        return quicksort([*filter(lambda x: x < pivot, lst)]) + [pivot] * lst.count(pivot) + quicksort([*filter(lambda x: x > pivot, lst)])
    return lst

if __name__ == '__main__':
    lst = [1, 2, 5, 6, 0, 3, 6, 4, 10, -9]

    print('Bubble sort\t', bubble(lst))
    print('Insertion sort\t', insertion(lst))
    print('Merge sort\t', merge_sort(lst))
    print('Quicksort\t', quicksort(lst))

############################################ Counting Sort ############################################
def counting_sort(lst):
    ##### Handling negatices #####
    negs = []
    if any(item < 0 for item in lst):
        poss = []
        for item in lst:
            negs.append(item) if item < 0 else poss.append(item)
        lst = poss
    
    ###### Main part ######
    k = max(lst)
    count = [0] * (k + 1)
    output = [None] * len(lst)
    
    for i in range(len(lst)):
        count[lst[i]] += 1

    for i in range(1, k+1):
        count[i] += count[i-1]

    for i in range(len(lst)-1, -1, -1):
        j = lst[i]
        count[j] -= 1
        output[count[j]] = lst[i]

    ##### Counting sort for negative #####
    if negs:
        output = list(map(lambda x: -x, counting_sort(list(map(abs, negs)))))[::-1] + output
    return output

def bsearch(lst, target):
  assert all(curr >= prev for curr, prev in zip(lst[1:], lst)), "Anticipated an increasing(ascending) ordered list"
  lo, hi = 0, len(lst)
  while hi > lo:
    mid = lo + (hi - lo) // 2
    if lst[mid] == target:
      return mid
    elif lst[mid] < target:
      lo = mid + 1
    else:
      hi = mid
  return -1

lst = [*range(10)]
print(bsearch(lst), 1)

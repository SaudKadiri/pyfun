def lsearch(lst, target):
  for i, ele in enumerate(lst):
    if ele == target:
      return i
  return -1

lst = [*range(10)]
print(lsearch(lst, 1))

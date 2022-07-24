import comparison_sorts
import random
from timeit import default_timer as timer
from datetime import timedelta

if __name__ == '__main__':
    sorts = [(x.replace('_', ' ').capitalize(), y) for x, y in comparison_sorts.__dict__.items() if 'sort' in x]
    lst = [*range(-24000, 24000)]
    random.shuffle(lst)
    print('Intitially:', lst if len(lst) <= 24 else '...')
    print('-'*139, '+', sep='')
    print('Algorithm\t|\t\t\t\t\t\t\tOutput\t\t\t\t\t\t|\tTime\t\t|')
    print('-'*139, '+', sep='')
    for name, algo in sorts:
        start = timer()
        ans = algo(lst.copy())
        end = timer()
        print(f'{name}\t|\t', ans if len(ans) <= 24 else '\t\t\t\t\t\t...\t\t\t\t\t', '\t|', end=' ')
        print(timedelta(seconds=end-start), end='\t|\n')  
        print('-'*139, '+', sep='')

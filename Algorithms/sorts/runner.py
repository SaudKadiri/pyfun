import comparison_sorts as csorts
import random
from timeit import default_timer as timer
from datetime import timedelta
import distribution_sorts as dsorts

if __name__ == '__main__':
    is_sorted = lambda lst: all([prev <= curr for prev, curr in zip(lst, lst[1:])])
    lst = [*range(-12, 12)] + [*range(-120, 120)]
    random.shuffle(lst)
    sorts = {}
    for name, algo in (csorts.__dict__ | dsorts.__dict__).items():
        if 'sort' in name:
            name = name.replace('_', ' ').capitalize()
            print('Performing:', name, '...')
            start = timer()
            ans = algo(lst.copy())
            end = timer()
            sorts[name] = {"output": ans, "time": timedelta(seconds=end-start)}

    sorts = sorted(sorts.items(), key=lambda x: x[1]["time"])

    print('Intitially:', lst if len(lst) <= 24 else '...')
    print('-'*139, '+', sep='')
    print('Algorithm\t|\t\t\t\t\t\t\tOutput\t\t\t\t\t\t|\tTime\t\t|')
    print('-'*139, '+', sep='')

    for name, info in sorts:
        print(f'{name}\t|\t', info["output"] if len(info["output"]) <= 24 else f'\t\t\t\t\t\t{is_sorted(info["output"])}\t\t\t\t\t', '\t|', end=' ')
        print(info["time"], end='\t|\n')  
        print('-'*139, '+', sep='')
    

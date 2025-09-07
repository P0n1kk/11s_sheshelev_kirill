from itertools import permutations

graph = {'A': set('BCDH'),
         'B': set('AC'),
         'C': set('ABI'),
         'D': set('AEF'),
         'E': set('DG'),
         'F': set('DGH'),
         'G': set('EFI'),
         'H': set('AFI'),
         'I': set('CGH')}

templ = {1: [6, 9],
         2: [3, 5, 7],
         3: [2, 4, 9],
         4: [3, 6, 7],
         5: [2, 8],
         6: [1, 4, 8, 9],
         7: [2, 4, 8],
         8: [5, 6, 7],
         9: [1, 3, 6]}

for p in permutations('ABCDEFGHI'):
    chk = {p[k-1]: set(p[i-1] for i in v) for k, v in templ.items()}
    if chk == graph:
        print('1 2 3 4 5 6 7 8 9')
        print(*p)
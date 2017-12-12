
L = [1, 2, 3, -1, -1]
L = [-1, 1, -1, 1, -1]
n = len(L)
indices = list(range(n))

def sums(L):
    pool = []
    for n in range(len(L)):
        for start in range(n):
            for step in range(1, n+1):
                indices = list(range(start,n,step))
                if indices not in pool:
                    yield sum([L[idx] for idx in indices])
                    pool.append(indices)
    print(sorted(pool))

K = [s for s in sums(L)]
print(max(K))

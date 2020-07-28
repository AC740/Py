
finonacci_cache = {}

def finonacci(n):
    if n == 0:
        return
    if n==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        if n-1 not in finonacci_cache.keys():
            finonacci_cache[n-1] = finonacci(n-1)
        if n-2 not in finonacci_cache.keys():
            finonacci_cache[n-2] = finonacci(n-2)
        return finonacci_cache[n-1] + finonacci_cache[n-2]


print(finonacci(100))


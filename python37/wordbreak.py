def wordbreak(n, lst):
    # n = "andrewchoi"
    # lst = ['and', 'rew', 'choi']
    if len(n) == 0:
        return True

    for i in range(len(lst)):
        result = False
        if lst[i] == n[:len(lst[i])]:
            result = wordbreak(n[len(lst[i]):], lst)
        if result:
            return True
    return False

n = "andrewchoi"
lst = ['and', 'rew', 'choi']

print(wordbreak(n, lst))
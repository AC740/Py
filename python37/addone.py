
def add_one(lst):
    result = lst
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == 9:
            result[i] = 0
        else:
            result[i] += 1
            return result 
    if sum(result) == 0:
        result.insert(0, 1)
        return result
    # return result
# 3 

lst = [9,9,9]
print(add_one(lst))


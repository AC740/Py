
import functools 

def missingnumberSum(lst):
    missingcount = sum(i for i in range(lst[0], lst[-1]+1)) - functools.reduce(lambda x, y : x + y, lst)
    print(sum(i for i in range(lst[0], lst[-1]+1)))
    print(functools.reduce(lambda x, y : x + y, lst))
    return missingcount

def missingnumberXor(lst):
    sequenceXor = functools.reduce(lambda x, y : x ^ y, [i for i in range(lst[0], lst[-1]+1)])
    inputXor = functools.reduce(lambda x, y : x ^ y, lst)
    resultXor = sequenceXor ^ inputXor
    return resultXor

# lst = [3,4,5,6,7,10,11,12]
lst = [1,2,4]
print(missingnumberSum(lst))
print(missingnumberXor(lst))


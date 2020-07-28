


print(dir())

testdictionary = {"aapl" : 100, "tsla": 200, "LIT": 50, "QQQ":20, "qqq": 20, "AAPL": 100}

a = list(sorted(testdictionary.items(), key = lambda x : (x[1], x[0])))

print(a)

a = "teststERdf"
result = []
for i in a:
    if i.isupper():
        result.append(i)
print(result)






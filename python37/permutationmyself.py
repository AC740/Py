
def permutation(strin):
    if len(strin) == 1:
        return [strin]
    
    firstchar = strin[0]
    restchars = permutation(strin[1:])

    result = []
    for char in restchars:
        for i in range(len(char)+1):
            result.append(char[:i] + firstchar + char[i:])
    
    return result


teststring = "abcde"

for i in range(len(teststring)+1):
    print(i, teststring[:i], teststring[i:], sep=" ")



# print(permutation('abc'))

    # def permutation(strin):
    #     if len(strin) == 1:
    #         return [strin]

    #     restword = permutation(strin[1:])
    #     firstword = strin[0]

    #     result = []

    #     for rword in restword:
    #         for i in range(len(rword)+1):
    #             result.append(rword[:i]+firstword+rword[i:])
    #     return result


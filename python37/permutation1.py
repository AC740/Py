

if __name__ == '__main__':
    stringin = "HACK" 
    numberOfp = 2


    def permutation(strin):
        if len(strin) == 1:
            return [strin]

        restword = permutation(strin[1:])
        firstword = strin[0]

        result = []

        for rword in restword:
            for i in range(len(rword)+1):
                result.append(rword[:i]+firstword+rword[i:])
        return result


    print(permutation("abc"))

    for i in range(2):
        print(i)

    strin = "abc"

    print(strin[0:])
    print(strin[1:])
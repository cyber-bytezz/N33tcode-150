if len(S) != len(T):
    return False

countS , countT = {} , {}

for i in range(len(s)):
    countS[s[i]] = 1+countS.get(s[i], 0)
    countT[t[i]] = 1+countT.get(T[i] ,0)

    return countS == countT
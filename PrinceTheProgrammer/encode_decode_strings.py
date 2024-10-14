class Solution:
    def encode(self, strs):
        FinalList=[]
        for i in strs:
            NewStr=''
            for j in range(0,len(i)):
                NewStr+=chr(abs(36-ord(i[j])))
            FinalList.append(NewStr)
        return FinalList

    def decode(self, s):
        FinalList=[]
        for i in s:
            NewStr=''
            for j in range(0,len(i)):
                NewStr+=chr(ord(i[j])+36)
            FinalList.append(NewStr)
        return FinalList

class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list) # Dictionary in which we are mapping the CharCount of anagrams
        # Go through every string given in the input 
        for s in strs:
            count=[0]*26 # This is the inital array of 0's for a...z
            # Now we will go through every char in the string and map the characters in a immutable tuple like this 
            for c in s:
                count[ord(c)-ord("a")] +=1 # Here we are using ord -> which is the ASCII order for character.
                # And as we know that the 'a' starts from 97 in ASCII type.
                # So we have used this thing here where the current char number will be subtrated from the char number of a.
                # For e.g. -> 
                # According to ASCII a-> 97, b-> 98
                # If my char(c) is also a then 
                # a - a == 97-97 == 0
                # And if my char(c)is b->98 then
                # b - a == 98-97 == 1 and so on here I am increasing the result number by +=1 
                # Now the resultant will be our key so,
            key = tuple(count)
                # If the key is not in the dictionary then we will appen it like this 
            res[key].append(s) # Here the s is string which is unique for each char and we have assigned tuples for it so it can't be immutable 
                #Now we will be returning the values in the res 

        return list(res.values())

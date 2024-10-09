class Solution(object):
    def containsDuplicate(self, nums):
        k = nums
        l = set(k)
        if len(k) == len(l):
            return False
        else:
            return True

k = [1,2,3,4]
j = Solution()
j.containsDuplicate(k)
        

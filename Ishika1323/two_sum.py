class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range (0,len(nums)):
            for j in range (1,len(nums)):
                if (nums[i]+nums[j] == target and i!=j and j>i) :
                    ans.append(i)
                    ans.append(j)
                    
        return ans
        
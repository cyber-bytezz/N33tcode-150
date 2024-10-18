class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        set1 = {}
        for i in range(len(nums)):
            if nums[i] not in set1:
                set1[(target - nums[i])] = i
            else:
                return [set1[nums[i]],i]

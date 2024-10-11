class Solution:
    def containsDuplicate(self, nums: list[int]):
        return False if len(set(nums))==len(nums) else True

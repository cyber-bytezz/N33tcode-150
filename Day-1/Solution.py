class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        DataSet=set(nums)
        return True if len(DataSet)!= len(nums) else False

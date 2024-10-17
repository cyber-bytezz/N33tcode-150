class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        a = [1]*l

        for i in range(1, l):
            a[i] = a[i-1] * nums[i-1]

        m = 1
        for i in range(l-1, -1, -1):
            a[i] *= m
            m *= nums[i]

        return a

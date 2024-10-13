class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Map = {} # Hashmap with val : index

        # Loop through array
        for i,n in enumerate(nums):
            # Cal diff b/w target and current num
            diff = target - n
            
            # Check if the diff exists in Map
            if diff in Map:
                #If it exists then return the index of current element and index of the diff element
                return[i,Map[diff]]
            # If doesn't exists then add that in the map with it's index
            Map[n] = i # Val : Index
        #If the numbers add up to the target, return none
        return

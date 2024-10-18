class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in frequency.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:  
                result.extend(buckets[i])
                if len(result) >= k:  
                    return result[:k]

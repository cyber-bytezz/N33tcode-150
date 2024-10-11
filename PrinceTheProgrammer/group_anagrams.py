class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sort=''.join(sorted(s))
            res[sort].append(s)
        return list(res.values())

class Solution(object):
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram[sorted_str].append(s)

        return anagram.values()

r = ["eat","tea","tan","ate","nat","bat"]
j = Solution()
j.groupAnagrams(r)

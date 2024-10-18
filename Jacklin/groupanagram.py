class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        
        for word in strs:
            sortedWord = ''.join(sorted(word))  
            anagramGroups[sortedWord].append(word) 
        
        return list(anagramGroups.values())
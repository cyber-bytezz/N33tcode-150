class Solution {
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        Map <String, List <String>> anagrams = new HashMap<>();

        for(String s : strs)
        {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);

            if(!anagrams.containsKey(key))
            {
                anagrams.put(key, new ArrayList<>());
            }

            anagrams.get(key).add(s);
        }

        return new ArrayList<>(anagrams.values());
    }
}


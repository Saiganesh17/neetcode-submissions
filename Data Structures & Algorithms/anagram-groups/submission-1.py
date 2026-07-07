class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups= defaultdict(list)
        for string in strs:
            sorted_key= ''.join(sorted(string))
            anagram_groups[sorted_key].append(string)
        return list(anagram_groups.values())
        #Time complexity is O(N* K * logK)
        #space complexity is O(N*k)
        #Pitfall1: Using mutable objects as dictionary keys
        #pitfall2: Incorrect character frequency counting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        char_count= Counter(s)
        for char in t:
            char_count[char]-= 1
            if char_count[char]<0:
                return False
        return True
        #Time and space complexity is O(n) & O(C)
        #Pitfall1: Forgetting the length check
        #Pitfall2: Using default dictionary behaviour incorrectly
        #Pitfall3: Inefficient double pass verification
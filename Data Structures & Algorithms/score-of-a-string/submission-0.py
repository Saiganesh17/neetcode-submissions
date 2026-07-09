class Solution:
    def scoreOfString(self, s: str) -> int:
        from itertools import pairwise
        ascii_values= map(ord, s)
        score = sum(abs(a- b) for a,b in pairwise(ascii_values))
        return score
        #Time and space complexity is O(n) & O(1) respectively
        #pitfall1: Python version compatibility issue
        #pitfall2: Edge case: Empty or single character string
        #pitfall3: Misunderstanding ASCII vs Unicode
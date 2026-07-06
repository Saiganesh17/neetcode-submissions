class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            n &= n - 1
            count+=1
        return count
        #Time complexity id O(k) & space complexity is O(1)
        #Pitfall1: Attempting to use string conversion for bit counting
        
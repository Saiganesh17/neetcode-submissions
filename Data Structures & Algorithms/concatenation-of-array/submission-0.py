class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+ nums
        #Time and space complexity is O(n) & O(n) respectively
        #pitfall1: Modifying the original array instead of creating a new one
        #pitfall2: Using multiplication operator incorrectly
        #pitfall3: Manual loop implementation errors
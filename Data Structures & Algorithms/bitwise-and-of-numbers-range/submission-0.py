class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right= right & (right-1)
        return right
        #Time and space complexity is O(logn ) and O(1) respectively
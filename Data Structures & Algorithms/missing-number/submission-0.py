from functools import reduce
from operator import xor
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, (index^ value for index, value in enumerate(nums, 1)))
    #Time and space complexity is O(n) & O(1)
    #pitfall1: Misunderstanding the enumeration starting point
    #pitfall2: not including all the numbers in range[0,n]
    #pitfall3: alternative correct solution not recognized 
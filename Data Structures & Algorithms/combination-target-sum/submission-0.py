from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(start, remaining, path):
            if remaining==0:
                res.append(path[:])
                return 
            for i in range(start, len(nums)):
                if nums[i]<=remaining:
                    path.append(nums[i])
                    backtrack(i,remaining -nums[i], path)
                    path.pop()
        backtrack(0, target,[])
        return res 
        #Time and space complexity is O(2^ (target/ min(nums))) and O(target/min(nums)) respectively
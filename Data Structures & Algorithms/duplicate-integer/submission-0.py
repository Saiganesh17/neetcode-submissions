class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums= sorted(nums)
        return any(a == b for a,b in pairwise(sorted_nums))
        #Time and space complexity  is O(N* log(N)) & O(N)
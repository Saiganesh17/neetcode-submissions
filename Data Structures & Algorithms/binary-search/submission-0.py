class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        first_true_index=-1
        while left<= right:
            mid= (left+right)//2
            if nums[mid]>= target:
                first_true_index= mid
                right= mid-1
            else:
                left= mid+1
        if first_true_index!= -1 and nums[first_true_index]==target:
            return first_true_index
        return -1
        #Time and space complexity is O(log n ) and O(1 ) respectively
        
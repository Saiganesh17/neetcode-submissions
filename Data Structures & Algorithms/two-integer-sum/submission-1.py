class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index={}
        for index, num in enumerate(nums):
            complement= target- num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num]=index
        #Time and space complexity is O(N) & O(N)
        # N is the length of the array
        #Pitfall1: using the same element twice
        #Pitfall2: Overwriting dictionary values with duplicate numbers
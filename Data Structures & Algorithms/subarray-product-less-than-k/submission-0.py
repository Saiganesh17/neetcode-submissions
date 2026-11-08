
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        product = 1
        ans = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            ans += right - left + 1

        return ans
        #Time and space is O(n) and O(1) respectively
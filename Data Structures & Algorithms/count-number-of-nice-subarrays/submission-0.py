
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count = 0
        ans = 0
        prefix = {0: 1}

        for num in nums:
            if num % 2 == 1:
                count += 1

            ans += prefix.get(count - k, 0)

            prefix[count] = prefix.get(count, 0) + 1

        return ans
        #Time and space is O(n) and O(n) respectively

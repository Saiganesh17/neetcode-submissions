class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to enable two-pointer technique
        nums.sort()
        n = len(nums)
        result = []

        # Iterate through the array, fixing the first element
        for i in range(n - 2):
            # Early termination: if the smallest number is positive, no zero sum possible
            if nums[i] > 0:
                break

            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum to -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    # Sum is too small, move left pointer to increase the sum
                    left += 1
                elif current_sum > 0:
                    # Sum is too large, move right pointer to decrease the sum
                    right -= 1
                else:
                    # Found a valid triplet with sum equal to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
        #Time complexity is O(n^2)
        #Space complexity is O(logn)
        #Pitfall1: Incorrect duplicate handling after finding a valid triplet
        #Pitfall2: Off by one error in duplicate skipping logic
        #Pitfall3: Forgetting to check bounds before skipping duplicates
        #Pitfall4: Skipping duplicates for the first element incorrectly
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num_strings= len(strs)
        dp=[[[0]* (n+1) for _ in range(m+1)] for _ in range(num_strings+1)]
        for string_idx, current_string in enumerate(strs, 1):
            zeros_count= current_string.count("0")
            ones_count= current_string.count("1")
            for zeros_limit in range(m + 1):
                # Iterate through all possible states of ones (0 to n)
                for ones_limit in range(n + 1):
                    # Option 1: Don't include current string
                    dp[string_idx][zeros_limit][ones_limit] = dp[string_idx - 1][zeros_limit][ones_limit]
                  
                    # Option 2: Include current string if we have enough zeros and ones
                    if zeros_limit >= zeros_count and ones_limit >= ones_count:
                        dp[string_idx][zeros_limit][ones_limit] = max(
                            dp[string_idx][zeros_limit][ones_limit],
                            dp[string_idx - 1][zeros_limit - zeros_count][ones_limit - ones_count] + 1
                        )
      
        # Return the maximum strings that can be formed with m zeros and n ones
        return dp[num_strings][m][n]
        #Time and space complexity is O(sz* m* n) and O(sz* m* n ) respectively
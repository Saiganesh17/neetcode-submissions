from typing import List
from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Find the minimum cost to reach the top of the staircase.
        You can start from either step 0 or step 1, and from each step
        you can climb either 1 or 2 steps.
      
        Args:
            cost: List where cost[i] is the cost of stepping on the ith step
          
        Returns:
            Minimum cost to reach the top (beyond the last step)
        """
      
        @cache
        def dfs(current_step: int) -> int:
            """
            Calculate minimum cost starting from current_step to reach the top.
          
            Args:
                current_step: Current position on the staircase
              
            Returns:
                Minimum cost from current_step to the top
            """
            # Base case: if we've reached or passed the top, no additional cost
            if current_step >= len(cost):
                return 0
          
            # Pay the cost of current step and choose minimum between:
            # - Taking 1 step forward
            # - Taking 2 steps forward
            one_step = dfs(current_step + 1)
            two_steps = dfs(current_step + 2)
          
            return cost[current_step] + min(one_step, two_steps)
      
        # Can start from either step 0 or step 1, return the minimum
        start_from_zero = dfs(0)
        start_from_one = dfs(1)
      
        return min(start_from_zero, start_from_one)
        #Time and space complexity is O(n) and O(n ) respectively
        #pitfall1: Misunderstanding the problems end condition
        #pitfall2: Forgetting to consider both starting points
        #pitfall3: Incorrect handling of small arrays
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n= len(heights)
        stack=[]
        left_boundaries= [-1]*n
        right_boundaries= [n]* n
        for i, current_height in enumerate(heights):
            while stack and heights[stack[-1]]>= current_height:
                right_boundaries[stack[-1]]= i
                stack.pop()
            if stack:
                left_boundaries[i]= stack[-1]
            stack.append(i)
        max_area= max(height * (right_boundaries[i]- left_boundaries[i] - 1)
        for i, height in enumerate(heights))
        return max_area
        #Time and space complexity is O(n) & O(n) respectively
        #pitfall1: Handling equal heights inconsistently
        #pitfall2: Forgetting to handle remaining stack elements
        #pitfall3: Off by one error in width calculation 
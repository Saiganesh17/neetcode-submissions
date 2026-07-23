class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index:int)->None:
            if index>=n:
                result.append(current_permutation[:])
                return
            for j, num in enumerate(nums):
                if not used[j]:
                    used[j]=True
                    current_permutation[index]=num
                    backtrack(index+ 1)
                    used[j]= False
        n=len(nums)
        used= [False]*n
        current_permutation=[0]*n
        result=[]
        backtrack(0)
        return result
        # 0 1  1 2  1 2 3  backtrack index 3 2 1 0
        #Time complexity os O(n!* n) and space complexity is O(n) respectively
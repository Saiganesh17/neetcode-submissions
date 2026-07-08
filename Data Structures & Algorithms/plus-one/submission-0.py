class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n= len(digits)
        for i in range(n-1, -1, -1):
            digits[i]+= 1
            digits[i] %= 10
            if digits[i]!= 0:
                return digits
        return [1]+ digits
        #Time complexity is O(n)
        #Space complexity is O(1)
        #Pitfall1: Attempting string conversion approach
        #Pitfall2: Forgetting to handle all 9's cases
        #Pitfall3: Modifying input array without considering immutability requirements
        
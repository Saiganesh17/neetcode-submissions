class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK= 0xFFFFFFFF
        MAX_INT= 0x7FFFFFFF
        a= a& MASK
        b= b& MASK
        while b!= 0:
            carry= ((a& b)<< 1)& MASK
            a= a^b
            b= carry
        if a> MAX_INT:
            return ~(a^MASK)
        else:
            return a
        #Time complexity and space complexity is O(1) & O(1) respectively
        #pitfall1: forgetting to mask intermediate results in the loop
        #pitfall2: incorrect handling of negative number conversion
        #pitfall3: not masking initial inputs
        
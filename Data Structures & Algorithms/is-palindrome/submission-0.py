class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index=0
        right_index= len(s)-1

        while left_index < right_index:
            if not s[left_index].isalnum():
                left_index+=1
            elif not s[right_index].isalnum():
                right_index-= 1
            elif s[left_index].lower() != s[right_index].lower():
                return False
            else:
                left_index+= 1
                right_index-=1
        return True
        #Time and space complexity is O(N) & O(1)
        #Pitfall1: incorrect pointer movement logic
        #Pitfall2: Infinite loop when all characters are non-alpha numeric
        #Pitfall3: using <= instead of < in the while condition
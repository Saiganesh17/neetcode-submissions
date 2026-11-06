class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        current = []

        def backtrack(i):
            if i == len(digits):
                result.append("".join(current))
                return

            for char in phone[digits[i]]:
                current.append(char)
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result
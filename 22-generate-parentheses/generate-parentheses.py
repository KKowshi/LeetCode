from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, left, right):
            # If the current string is of required length, add to result
            if len(s) == 2 * n:
                res.append(s)
                return

            # Add '(' if we still have left ones to add
            if left < n:
                backtrack(s + '(', left + 1, right)

            # Add ')' only if it won't exceed the number of '('
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack("", 0, 0)
        return res
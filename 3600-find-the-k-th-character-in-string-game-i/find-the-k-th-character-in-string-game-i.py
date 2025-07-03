class Solution:
    def kthCharacter(self, k: int) -> str:
        res = 'a'
        while len(res) < k:
            # use the length so far, not the last letter
            ch = Solution.next_char(len(res))
            res += ch
        return res[k - 1]

    @staticmethod
    def next_char(n: int) -> str:
        """Return the letter determined by popcount(n)."""
        shifts = n.bit_count()          # number of 1-bits in n
        return chr(ord('a') + shifts % 26)

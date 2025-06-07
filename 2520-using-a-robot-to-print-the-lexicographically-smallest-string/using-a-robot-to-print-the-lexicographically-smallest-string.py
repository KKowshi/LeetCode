class Solution:
    def smallest(self, right_freq):
        for i in range(26):
            if right_freq[i] > 0:
                return chr(97 + i)
        return 'z'

    def robotWithString(self, s: str) -> str:
        n = len(s)
        right_freq = [0] * 26
        for c in s:
            right_freq[ord(c) - ord('a')] += 1

        t = []
        res = []
        pos = 0
        while pos < n:
            t.append(s[pos])
            right_freq[ord(s[pos]) - ord('a')] -= 1

            while t and ord(t[-1]) <= ord(self.smallest(right_freq)):
                res.append(t.pop())
            pos += 1
        return ''.join(res)
        
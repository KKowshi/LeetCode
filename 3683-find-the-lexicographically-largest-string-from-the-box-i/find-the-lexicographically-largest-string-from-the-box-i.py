class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word

        i = 0
        j = 1
        gap = 0

        # Find largest suffix
        while j + gap < n:
            if word[i + gap] == word[j + gap]:
                gap += 1
            elif word[i + gap] < word[j + gap]:
                save = i
                i = j
                j = max(j + 1, save + gap + 1)
                gap = 0
            else:
                j = j + gap + 1
                gap = 0
        return word[i:i + n - numFriends + 1]
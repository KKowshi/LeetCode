from typing import List

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Count the number of possible intended strings whose length ≥ k,
        given the final word that may contain duplicated (long-pressed) runs.

        • word.length ≤ 5 × 10⁵, k ≤ 2000                       –-->  O(k²) in worst case
        • mod = 1_000_000_007                                   –-->  64-bit safe
        """
        MOD = 1_000_000_007          # 10⁹ + 7 (prime)

        # ------------------------------------------------------------
        # 1.  Compress `word` into runs:  "aaabb"  ->  [3, 2]
        # ------------------------------------------------------------
        runs: List[int] = []
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                runs.append(cnt)
                cnt = 1
        runs.append(cnt)             # push the final run
        m = len(runs)                # number of runs

        # ------------------------------------------------------------
        # 2.  Total possibilities without length restriction
        #     Each run of size r lets Alice keep 1…r characters
        #     ⇒  r possibilities per run, independent
        # ------------------------------------------------------------
        total = 1
        for r in runs:
            total = (total * r) % MOD

        # ------------------------------------------------------------
        # 3.  If the *minimum* length we could ever get (one char
        #     per run) is already ≥ k, every possibility is valid.
        # ------------------------------------------------------------
        if m >= k:                   # because min‐len = m (≥ k)
            return total

        # ------------------------------------------------------------
        # 4.  Otherwise we must subtract the “invalid” originals
        #     whose length < k.  k ≤ 2000,  m < k  ⇒  O(m·k²) ≤ 4 M.
        #
        #     f[j] – ways to obtain EXACT length j with processed runs
        #     g[j] – prefix sum  Σ_{t ≤ j} f[t]     (helps w/ O(1) range)
        #
        #     Transition for a run of length r:
        #         f_new[j] = Σ_{t = 1…min(r, j)} f_prev[j − t]
        #
        #     Using prefix sums:
        #         f_new[j] = g_prev[j-1] − g_prev[j − r − 1]  (if index ≥ 0)
        # ------------------------------------------------------------
        f = [1] + [0]*(k - 1)        # f[0] = 1 (empty string before any run)
        g = [1] + [0]*(k - 1)        # g = prefix(f); here g[j] = 1 for all j ≥ 0
        for j in range(1, k):
            g[j] = (g[j - 1] + f[j]) % MOD

        for r in runs:
            f_new = [0]*k

            # length 0 is impossible once we pick from current run (must pick ≥ 1)
            for j in range(1, k):
                upper = g[j - 1]                    # Σ f_prev[.. j-1]
                lower_idx = j - r - 1               # Σ f_prev[.. j-r-1]
                if lower_idx >= 0:
                    upper -= g[lower_idx]
                f_new[j] = upper % MOD

            # rebuild g_new as running prefix of f_new
            g_new = [f_new[0]] + [0]*(k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % MOD

            f, g = f_new, g_new                     # move to next run

        # g[k-1] now holds the number of originals with length ≤ k-1  (invalid)
        valid = (total - g[k - 1]) % MOD
        return valid

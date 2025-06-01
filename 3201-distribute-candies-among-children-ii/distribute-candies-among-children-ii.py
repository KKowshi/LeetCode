class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def calc(val):
            if val <0:
                return 0
            return ((val+1) * (val+2)) // 2

        total = calc(n)
        extra = 3 * calc(n-(limit+1))
        doubleextra = 3 * calc(n-2 * (limit+1))
        common = calc(n-3 * (limit+1) )

        return total-extra+doubleextra-common
        

        
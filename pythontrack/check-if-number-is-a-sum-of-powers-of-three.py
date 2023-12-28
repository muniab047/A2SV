class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = int(n ** (1/3))
        while i > -1:
            if n >= 3**i:
                n -= 3**i
            i-=1
        return n==0
class Solution:
    def mySqrt(self, x: int) -> int:
        
        sqr=[pow(i,2) for i in range(46341)]
        return bisect_right(sqr,x)-1


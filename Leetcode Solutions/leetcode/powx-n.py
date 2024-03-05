class Solution:
    def myPow(self, x: float, n: int) -> float: 
        if n<0:
            return 1/self.myPow(x, abs(n))
        if n==0:
            return 1
        if n==1 :
            return x
        t = self.myPow(x,n//2)
        if n%2==0:           
            return t * t
        return t*t*x
       
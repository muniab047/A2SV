class Solution:
    def isPalindrome(self, x: int) -> bool:
        x3=str(x)
        x2= ''.join(reversed(x3))

        if(x3==x2):
            return True
        else:
            return False
        
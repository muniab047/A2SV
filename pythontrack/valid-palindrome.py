class Solution:
    def isPalindrome(self, s: str) -> bool:

        ss=''
        for char in s:
            if char.isalnum():
                ss+=char.lower()

        

        if ss==ss[::-1]:
            return True

        return False
        
        
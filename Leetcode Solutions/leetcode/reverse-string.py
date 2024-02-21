class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        # for i in range(n//2):
        #     s[i], s[len(s)-i-1]= s[len(s)-i-1],s[i]

        def reverse(i,j):
            if i>j:
                return
            s[i], s[j]= s[j],s[i]
            reverse(i+1,j-1)
        reverse(0,len(s)-1)
        
        


        
        



        
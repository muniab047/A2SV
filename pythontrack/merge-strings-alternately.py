class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        for i in range(max(len(word1),len(word2))):
            if(len(word1)>=i+1):
                ans+=word1[i]

            if(len(word2)>=i+1):
                ans+=word2[i]
        return ans



        
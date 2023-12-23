class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans=''
        for j in range(len(min(strs, key=len))):
            for i in range(1,len(strs)):
                if(strs[0][j]!=strs[i][j]):
                    return ans

            ans+=strs[0][j]
        
        return ans
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=['q','w','e','r','t','y','u','i','o','p']
        row2=['a','s','d','f','g','h','j','k','l']
        row3=['z','x','c','v','b','n','m']

        ans=[]

        for i in range(len(words)):
            f=True
            if(words[i][0].lower() in row1):
                
                for char in words[i]:
                    if(char.lower() not in row1): 
                        f=False
                        break

            elif(words[i][0].lower() in row2):
            
                for char in words[i]:
                    if(char.lower() not in row2):
                        f=False
                        break
            elif(words[i][0].lower() in row3):
            
                for char in words[i]:
                    if(char.lower() not in row3):
                        f=False
                        break

            if f: ans.append(words[i])

        


        return ans

            

                    

            

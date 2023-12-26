class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        li=[]

        for i in range(len(words)):
            num=[]
            for j in range (len(words[i])):
                num.append(order.index(words[i][j]))
            li.append(num)


        if(li== sorted(li)):
            return True
        else:
            return False

        

        




        
        

        
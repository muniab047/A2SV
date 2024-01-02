class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        li=[]
        counter=0
        for i in range(len(strs)):
            li.append(list(strs[i]))

        li=list(zip(*li))
        li=[list(l) for l in li]
      
        

        for j in range(len(li)):
            if (li[j]!= sorted(li[j])):
                counter+=1

        return counter


        
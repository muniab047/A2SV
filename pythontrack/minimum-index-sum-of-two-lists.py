class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index={}
        for i in range(len(list1)):
            if(list1[i] in list2):
                j=list2.index(list1[i])
                summ=i+j
                index[list1[i]]=summ

        mini= min(index.values())
        ans=[key for key,value in index.items() if value==mini]

        return ans


        return list(index[maximum])


        
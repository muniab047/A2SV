class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        
        a=self.getRow(rowIndex-1)
        res=[1]
        for i in range(1,len(a)):
            num=a[i]+a[i-1]
            res.append(num)
        res.append(1)
        return res




        

        
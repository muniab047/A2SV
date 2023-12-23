class Solution:
    def average(self, salary: List[int]) -> float:
        salary=list(set(salary))
        salary.sort()
        summ= sum(salary[1:len(salary)-1])
        return summ/(len(salary)-2)
        
        
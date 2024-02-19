class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter=Counter(answers)
        rabbits=0
        for key in counter:
            rabbits+=(key+1)*(ceil(counter[key]/(key+1)))
        return rabbits
        
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(mid):
            counter = 1
            sum_ = 0
            for i in range(len(weights)):
                sum_ += weights[i]
                if i+1<len(weights) and sum_+weights[i+1] > mid:
                    counter += 1
                    sum_ = 0
            return counter


        left = max(weights)
        right = sum(weights)
        best = right

        while left <= right:
            mid = (left + right) // 2
            counter = getDays(mid)
            if counter > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return best


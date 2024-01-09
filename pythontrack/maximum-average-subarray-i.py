class Solution:
    def findMaxAverage(self, nums, k):
        start = 0
        end = 0
        _sum = 0.0

        v = []

        for i in range(len(nums)):
            if i < k:
                _sum += nums[i]
                if k - 1 == i:
                    v.append(_sum)
            else:
                _sum = _sum + nums[i] - nums[start]
                start += 1
                v.append(_sum)

        max_val = max(v)
        av = max_val / k
        return av


        
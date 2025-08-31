from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = s
        for i in range(1, len(nums)):
            if s < 0:
                s = nums[i]
            else:
                s += nums[i]
            if s > res:
                res = s
        return res

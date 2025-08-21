class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])   # first window sum
        best = curr

        for i in range(k, len(nums)):
            curr = curr - nums[i - k]   # remove the element that goes out
            curr = curr + nums[i]       # add the new element that comes in

            if curr > best:
                best = curr

        return best / k

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # i = 0
            for j in range(i + 1, len(nums)): # j = 2
               if nums[i] + nums[j] == target:
                return [i,j]
                
                
    
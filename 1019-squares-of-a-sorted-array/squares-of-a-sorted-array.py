class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        square_root = 0
        result = []

        for i in range(len(nums)):
            square_root = nums[i] ** 2
            result.append(square_root)
        result.sort()
        return result
            
        # 2nd approach

        # return sorted([i ** 2 for i in nums])
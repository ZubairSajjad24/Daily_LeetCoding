class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # First solution:

        # firstOccurance = -1
        # lastOccurance = -1

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         firstOccurance = i
        #         break
        
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == target:
        #         lastOccurance = i
        #         break

        # return [firstOccurance, lastOccurance]

        # Second solution:

        firstOccurance = -1
        lastOccurance = -1

        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right)//2 
            if (nums[mid] == target):
                firstOccurance = mid
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else: right = mid - 1

        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right)//2
            if (nums[mid] == target):
                lastOccurance = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1

            else: right = mid -1
        
        return [firstOccurance, lastOccurance]
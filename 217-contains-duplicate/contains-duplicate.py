from collections import Counter, defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                return True

            hmap[nums[i]] = nums[i] 
        
        return False




    # def containsDuplicate_counter(self, nums: List[int]) -> bool:
    #     counter = Counter(nums)
    #     #print(counter.most_common(1))
    #     return  counter.most_common(1)[0][1] > 1


    # def containsDuplicate_set(self, nums: List[int]) -> bool:
    #     return len(set(nums)) != len(nums)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res=[]
        for t in count.most_common(k):
            res.append(t[0])
        return res
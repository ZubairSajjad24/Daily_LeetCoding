class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for st in strs:
            ref = [0] * 26
            for i in st:
                ref[ord(i)-97] += 1
            k = tuple(ref)
            if k in res:
                res[k].append(st)
            else:
                res[k] = [st]
        
        return list(res.values())
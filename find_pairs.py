from collections import Counter
class Sol:
    def find_pairs(self,nums,k):
        res=0
        if k == 0:
            return max(list(Counter(nums).values()))
        nums=set(nums)
        for num in nums:
            if num+k in nums:
                res+=1
        return res

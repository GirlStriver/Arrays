class Solution:
    def Repeated(self, nums: List[int]) -> int:
        def repeated(nums):
            hashset={}
            for i in nums:
                if i in hashset:
                    hashset[i]+=1
                else:
                    hashset[i]=1
            
            for j in hashset:
                if hashset[j]>1:
                    return j
        return sum([i for i in range(len(nums)+1)])-sum(nums) , repeated(nums)
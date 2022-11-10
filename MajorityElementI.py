class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ls={}
        for i in list(set(nums)):
            ls[i]=nums.count(i)
        res=[i for i in ls.values()]
        res=[i for i in ls if ls[i]==max(res)]
        return ' '.join([str(i) for i in res])
            
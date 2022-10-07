from collections import Counter
class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        return [val for val,count in Counter(nums).items() if count>len(nums)//3]
        
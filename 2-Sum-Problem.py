class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
    
        for i in range(0, len(nums)):

            if target - nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i
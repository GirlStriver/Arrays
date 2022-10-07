class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sort = sorted(nums)
        count = 0
        for i in range(len(nums)-1, 0, -1):  # go reverse from most right
            del sort[ bisect_left(sort, nums[i]) ] # delete the current number
            target = 2 * nums[i]
            idx = bisect_left(sort, target+1)  # find where number greater than target
            count += len(sort) - idx
        return count
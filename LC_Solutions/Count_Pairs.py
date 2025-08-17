# Given a 0-indexed integer array nums of length n and an integer target, return the number
# of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pairs = 0 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if 0 <= i < j < len(nums) and nums[i] + nums[j] < target: 
                    print(nums[i],nums[j])
                    pairs += 1
                else:
                    continue
        return pairs

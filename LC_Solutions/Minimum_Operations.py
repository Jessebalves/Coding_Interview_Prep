#You are given an integer array nums and an integer k. You can perform the following operation any number of times:
#Select an index i and replace nums[i] with nums[i] - 1.
#Return the minimum number of operations required to make the sum of the array divisible by k.
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0 
        operations = 0

        for i in range(len(nums)):
            sum += nums[i]
        
        while sum % k != 0:
            operations += 1
            sum -= 1
        return operations

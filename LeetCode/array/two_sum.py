class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            num = target - v
            print(num)
            if num in nums and nums.index(num)!=i:
                return [i, nums.index(num)]

print(Solution().twoSum([3,2,4],6))

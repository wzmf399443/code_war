import fire
from collections import Counter


class Solution(object):
    def move_zeroes(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_nums = Counter(nums)[0]
        # nums = [i for i in nums if i != 0] + [0] * zero_nums
        nums = [i for i in nums if i != 0] + [i for i in nums if i == 0]
        return nums

# another solution
    def moveZeroes(self, nums):
        i = count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            count += 1


if __name__ == '__main__':
    fire.Fire(Solution)

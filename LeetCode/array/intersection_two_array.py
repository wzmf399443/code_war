from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        a = set(nums1)
        b = set(nums2)
        for k in a.intersection(b):
            ans += [k] * min(nums1[k], nums2[k])
        # nums1 = {k: v for k, v in Counter(nums1).items() if v > 1}
        # nums2 = {k: v for k, v in Counter(nums2).items() if v > 1}
        # for k in nums1:
        #     if k in nums2:
        #         ans += [k] * min(nums1[k], nums2[k])
        return ans


print(Solution().intersect([1, 2, 1, 2], [2, 2]))

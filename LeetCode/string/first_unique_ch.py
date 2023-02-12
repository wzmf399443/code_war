import fire
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)

        for k, v in count.items():
            if v == 1:
                ans = s.index(k)
                return ans
        return -1


if __name__ == '__main__':
    fire.Fire(Solution)

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        ans = re.match(r" *[+-]?[0-9]+", s)
        if ans:
            return max(min(int(ans.group()),2**31-1),-2**31)
        else:
            return 0


if __name__ == '__main__':
    print(Solution().myAtoi("www-001234"))

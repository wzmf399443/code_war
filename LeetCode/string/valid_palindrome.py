import fire
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]+', '', s)
        ans = True if s[::-1] == s else False
        print(s[::-1])
        return ans


if __name__ == '__main__':
    fire.Fire(Solution)

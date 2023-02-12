from collections import Counter
from typing import List


class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        minstr= min(S)
        maxstr= max(S)
        print(minstr, maxstr)
        prefix =""
        for i in range(len(minstr)):
            if minstr[i]!= maxstr[i]:
                break
            else:
                prefix = prefix+ minstr[i]

        return prefix

if __name__ == "__main__":
    strings = ['apple', 'aqicoteecwarawr', 'apartmeneeeet']
    print(Solution().longestCommonPrefix(strings))

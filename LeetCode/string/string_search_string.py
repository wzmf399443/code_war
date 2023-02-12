class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = haystack.find(needle)
        return ans

if __name__ == '__main__':
    print(Solution().strStr("eastset","x"))

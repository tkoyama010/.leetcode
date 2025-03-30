class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j]:
                    if k == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] and k > max_len:
                        start = i
                        max_len = k

        return s[start:start + max_len]

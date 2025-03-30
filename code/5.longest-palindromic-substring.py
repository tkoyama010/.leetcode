"""Module that contains a solution to the Longest Palindromic Substring problem."""

from __future__ import annotations

MAGIC_NUMBER = 2


class Solution:
    """Provides a method to solve the Longest Palindromic Substring problem."""

    def longest_palindrome(self: Solution, s: str) -> str:
        """Find the longest palindromic substring within a given string."""
        n = len(s)
        if n < MAGIC_NUMBER:
            return s

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for k in range(MAGIC_NUMBER, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j]:
                    if k == MAGIC_NUMBER:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and k > max_len:
                        start = i
                        max_len = k

        return s[start : start + max_len]

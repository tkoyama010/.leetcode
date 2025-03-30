"""Module that implements a solution to the Two Sum problem."""

from __future__ import annotations


class Solution:
    """Solve the Two Sum problem."""

    def two_sum(self: Solution, nums: list[int], target: int) -> list[int]:
        """Find two numbers in a list that add up to a given target."""
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

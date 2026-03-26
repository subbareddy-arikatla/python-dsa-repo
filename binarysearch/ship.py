"""Minimum capacity to ship packages within D days (LeetCode 1011).

Two functions:
 - ship_within_days(weights, D): classic problem, packages indivisible and must be shipped in order.
 - min_capacity_splittable(weights, D): if packages may be split arbitrarily (fractional), closed-form.

Usage:
    ship_within_days([1,2,3,4,5,6,7,8,9,10], 5)  # returns 15
"""

from typing import List
import math

def days_needed(capacity: int, weights: List[int]) -> int:
    """Return minimal number of days to ship all weights with given capacity (greedy).
    Assumes capacity >= max(weights).
    """
    days = 1
    current = 0
    for w in weights:
        if current + w <= capacity:
            current += w
        else:
            days += 1
            current = w
    return days

def ship_within_days(weights: List[int], D: int) -> int:
    """Return minimal integer capacity so we can ship weights within D days (contiguous order).
    Uses binary search + greedy counting (days_needed).
    Time: O(n log S) where S = sum(weights).
    """
    if not weights:
        return 0
    lo = max(weights)           # capacity must be at least largest single package
    hi = sum(weights)           # capacity at most sum (one day)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid, weights) <= D:
            hi = mid
        else:
            lo = mid + 1
    return lo

def min_capacity_splittable(weights: List[int], D: int) -> int:
    """If packages can be split arbitrarily, minimal capacity is:
       max(max(weights), ceil(sum(weights)/D)).
       (No binary search needed.)
    """
    if not weights:
        return 0
    return max(max(weights), math.ceil(sum(weights) / D))

# Example / quick test
if __name__ == "__main__":
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    print("Indivisible case (binary search):", ship_within_days(weights, D))  # expected 15
    print("Splittable case (closed form):", min_capacity_splittable(weights, D))  # expected max(10, ceil(55/5)=11) => 11
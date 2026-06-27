# 643. Maximum Average Subarray I

**Difficulty:** Easy

**Pattern:** Sliding Window (Fixed Size)

---

## Problem

Given an integer array `nums` consisting of `n` elements and an integer `k`, find the contiguous subarray of length `k` that has the maximum average value.

Return the maximum average.

---

## Example

Input:

nums = [1,12,-5,-6,50,3]
k = 4

Output:

12.75

Explanation:

Maximum sum window = [12,-5,-6,50]

Average = 51 / 4 = 12.75

---

## Intuition

A brute-force solution computes the sum of every subarray of size `k`, leading to repeated calculations.

Instead, maintain a **fixed-size sliding window**.

When moving the window:

- Add the new element entering the window.
- Remove the element leaving the window.

This updates the window sum in constant time.

---

## Approach

1. Compute the sum of the first `k` elements.
2. Store it as the maximum sum.
3. Slide the window one position at a time.
4. Update the current window sum by:
   - Adding the new element.
   - Removing the oldest element.
5. Keep track of the maximum window sum.
6. Return `max_sum / k`.

---

## Algorithm

1. Initialize `window_sum` with the first `k` elements.
2. Set `max_sum = window_sum`.
3. Iterate from index `k` to the end:
   - `window_sum += nums[right]`
   - `window_sum -= nums[right-k]`
   - Update `max_sum`
4. Return `max_sum / k`.

---

## Complexity Analysis

Time Complexity:

O(n)

Space Complexity:

O(1)

---

## Edge Cases

- k = 1
- k = len(nums)
- All negative numbers
- All positive numbers
- Mixed positive and negative numbers

---

## Key Takeaways

- This is a **Fixed-Size Sliding Window** problem.
- Avoid recomputing the sum for every window.
- Window updates take O(1) time.

---

## Similar Problems

- Minimum Size Subarray Sum
- Maximum Number of Vowels in a Substring
- Max Consecutive Ones III
- Longest Repeating Character Replacement
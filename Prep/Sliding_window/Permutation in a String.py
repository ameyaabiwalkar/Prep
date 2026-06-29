from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer than s2, no permutation is possible.
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        left = 0

        for right in range(len(s2)):

            # Expand the window by including the current character.
            window_count[s2[right]] += 1

            # Shrink the window if it exceeds the desired size.
            if right - left + 1 > len(s1):

                window_count[s2[left]] -= 1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # Check if the current window is a permutation of s1.
            if window_count == s1_count:
                return True

        return False
    
# Notes:
# TC: O(N)
# SC: O(1)
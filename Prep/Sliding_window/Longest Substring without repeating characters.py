class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set() # Checking for duplicates
        result=0
        left=0
        for right in range(len(s)):  # right keeps changing
            while s[right] in charSet:
                charSet.remove(s[left]) # shrink the window if character repeats
                left+=1
            charSet.add(s[right])
            result=max(result,right-left+1)
        return result             
        
#Notes:
# Input: "abcabcbb"
# Output: 3

# Sets: used for checking duplicates
# TC: O(n) traversing through the entire string

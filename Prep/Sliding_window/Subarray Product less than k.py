class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        prod=1
        res=0

        for right in range(len(nums)):
            prod=prod*nums[right]
            if prod>=k:
                while prod>=k and left<=right:
                    prod=prod/nums[left]
                    left=left+1
            res=res+right-left+1
        
        return res


# Notes:
# TC:O(N)
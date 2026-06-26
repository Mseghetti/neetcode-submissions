from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # early return for minimal input size 2
        if n == 2:
            return [nums[1], nums[0]]

        # first pass. output[i] holds product of nums[0..i-1]
        output = [1] * n
        prefix = 1
        for i in range(n): 
            output[i] = prefix
            prefix *= nums[i]

        # second pass. suffix holds product of nums[i+1..end]
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        
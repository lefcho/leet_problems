from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1

        while k < len(nums):
            prev = nums[k - 1]
            
            if prev == nums[k]:
                nums.pop(k)
            else:
                k += 1
        return k

s = Solution()
print(s.removeDuplicates([1]))
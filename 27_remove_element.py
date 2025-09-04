from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while val in nums:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        
        return len(nums)
    

s = Solution()
s.removeElement([3,2,2,3], 3)
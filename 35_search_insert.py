from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums)
        pm = None

        while top > bot:
            mid = (top + bot) // 2
            if mid == pm:
                return mid + 1
            pm = mid
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                top = mid
            else:
                bot = mid
            
        return mid
    

s = Solution()
print(s.searchInsert([1,2,5,6,7,8,9,10,13], 3))
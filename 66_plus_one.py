from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 1
        mult = 1
        while digits:
            n = digits.pop()
            result += n * mult
            mult *= 10
        
        return [int(d) for d in str(result)]
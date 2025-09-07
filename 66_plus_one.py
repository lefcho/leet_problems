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
    

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits
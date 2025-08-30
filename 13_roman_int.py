class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        sum = 0

        roman_hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for l in s:
            current = roman_hash[l]
            if stack:
                prev = stack[-1]
                

                if prev < current:
                    sum += current - prev * 2
                else:
                    sum += current
            else:
                sum += current
            stack.append(roman_hash[l])

        return sum
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = max(len(a), len(b))
        a = a.zfill(m)
        b = b.zfill(m)
        res = [0] * (m + 1)

        for i in range(m - 1, -1, -1):
            a_add = int(a[i])
            b_add = int(b[i])
            c = res[i + 1]

            current = a_add + b_add + c
            if current == 1:
                res[i + 1] = 1
            elif current == 2:
                res[i] = 1
                res[i + 1] = 0
            elif current == 3:
                res[i] = 1
                res[i + 1] = 1
        
        return ''.join(map(str, res)).lstrip('0') or '0'

s = Solution()
print(s.addBinary('10110', '111'))

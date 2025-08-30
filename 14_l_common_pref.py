from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        for w in strs:
            next_pref = ''

            for i in range(min(len(w), len(pref))):
                if w[i] == pref[i]:
                    next_pref += w[i]
                else:
                    break
            
            pref = next_pref

        return pref
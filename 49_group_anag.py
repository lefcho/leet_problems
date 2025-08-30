from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            key = tuple(sorted(s))
            anagram_map[key].append(s)

        for val in anagram_map.values():
            result.append(val)

        return result

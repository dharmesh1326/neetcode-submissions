from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        am=defaultdict(list)
        for s in strs:
            key=tuple(sorted(s))
            am[key].append(s)
        return list(am.values())
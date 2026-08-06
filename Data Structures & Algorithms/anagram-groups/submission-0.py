from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # only lowercase letters
        res = defaultdict(list)
        for word in strs:
            sortedStr = ''.join(sorted(word))
            res[sortedStr].append(word)
        return list(res.values())
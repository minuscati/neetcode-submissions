class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Answer = []
        seen = {}
        for s in strs:
            s_normal = str(sorted(s))
            if s_normal in seen:
                seen[s_normal].append(s)
            else:
                seen[s_normal] = [s]
        return [i for i in seen.values()]
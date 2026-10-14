class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary - keys anagrams (sorted), the values a list of possible anagrams
        # iterate throughout the list given i.e strs
        # add to the key

        anagrams = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)

        return [anagrams[key] for key in anagrams.keys()]

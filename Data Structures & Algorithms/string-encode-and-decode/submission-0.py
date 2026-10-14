class Solution:

    def encode(self, strs: List[str]) -> str:
        #loop thorugh the list of strings
        #encode something in front of it - length and then '|' so the rest can be differentiated
        ans = ''

        for s in strs:
            ans += str(len(s)) + '|'
            ans += s

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []

        i, j = 0, 0

        while i < len(s):
            while s[j] != '|':
                j += 1
            wordlen = int(s[i:j])
            ans.append(s[j + 1:j + 1 + wordlen])
            i = j = j + 1 + wordlen

        return ans
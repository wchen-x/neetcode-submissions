class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum() == False:
                continue
            l.append(str(i).lower())

        left = 0
        right = len(l) - 1
        
        while left < right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True

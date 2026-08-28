class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower()
        fin = ""

        for let in strs:
            if let.isalnum():
                fin += let

        l = 0
        r = len(fin) - 1

        while l < r:
            if fin[l] != fin[r]:
                return False

            l += 1
            r -= 1

        return True
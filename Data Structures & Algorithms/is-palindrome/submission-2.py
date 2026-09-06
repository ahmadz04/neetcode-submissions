class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringnew = ''.join(char.lower() for char in s if char.isalnum())
        leftptr = 0
        rightptr = len(stringnew) - 1
        while leftptr < rightptr:
            if stringnew[leftptr] != stringnew[rightptr]:
                return False
            else:
                leftptr += 1
                rightptr -= 1
        return True
        
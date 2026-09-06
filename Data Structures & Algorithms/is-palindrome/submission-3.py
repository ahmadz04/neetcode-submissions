class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftptr = 0
        rightptr = len(s) - 1

        while leftptr < rightptr:
            # Skip non-alphanumeric characters from the left
            while leftptr < rightptr and not s[leftptr].isalnum():
                leftptr += 1
            # Skip non-alphanumeric characters from the right
            while leftptr < rightptr and not s[rightptr].isalnum():
                rightptr -= 1

            if s[leftptr].lower() != s[rightptr].lower():
                return False

            leftptr += 1
            rightptr -= 1

        return True
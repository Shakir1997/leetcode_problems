class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (x == x[::-1]):
            return bool(1)
        else:
            return bool(0)
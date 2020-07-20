class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (len(num1) < 110) and (len(num2) < 110):
            x = int(num1)
            y = int(num2)
        return str(x*y)
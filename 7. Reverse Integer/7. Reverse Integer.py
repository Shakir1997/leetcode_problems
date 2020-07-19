class Solution:
    def reverse(self, x: int) -> int:
        neg_limit =-0x80000000
        pos_limit = 0x7fffffff
        if ((x & pos_limit) == x):
            x = str(x)
            x = x[::-1]
            x = int(x)
            if ((x & pos_limit) == x):
                return x
            else:
                return int(0)
        elif ((x & neg_limit) == neg_limit):
            x = abs(x)
            x = str(x)
            x = "-" + x[::-1]
            x = int(x)
            if ((x & neg_limit) == neg_limit):
                return int(x)
            else:
                return int(0)
        else:
            return int(0)
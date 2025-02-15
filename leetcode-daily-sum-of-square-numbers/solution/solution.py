class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if count % 2 and i % 4 == 3:
                    return False
            i += 1
        return c % 4 != 3
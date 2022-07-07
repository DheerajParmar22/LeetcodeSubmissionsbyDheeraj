class Solution:
    def fib(self, n: int) -> int:
        while n>=0:
            if n == 0 or n == 1:
                return n
            else:
                return self.fib(n-1)+self.fib(n-2)
        
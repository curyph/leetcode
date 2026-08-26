# RECURSION
class Solution:
    def climb_stairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climb_stairs(n - 1) + self.climb_stairs(n - 2)


# a = Solution()
# b = a.climb_stairs(4)
# print(b)

# DP BOTTOM UP 

class Solution:
    def climb_stairs(self, n):
        memo = {1:1, 2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n - 1) + f(n - 2)
                return memo[n]
        return f(n)
    

a = Solution()
b = a.climb_stairs(5)
print(b)
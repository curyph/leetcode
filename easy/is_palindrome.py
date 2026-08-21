class Solution:
    @classmethod
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            reverse_x = str(abs(x))[::-1]        
            a = True if x == int(reverse_x) else False
            return a
        else:
            reverse_x = str(x)[::-1]        
            a = True if x == int(reverse_x) else False
            return a



print(Solution.isPalindrome(-121))
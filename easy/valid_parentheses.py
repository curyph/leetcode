class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        char_list = []
        
        for c in s:
            if c in mapping:
                if char_list and char_list[-1] == mapping[c]:
                    char_list.pop()
                else:
                    return False
            else: 
                char_list.append(c)
        return True if not char_list else False



a = Solution()
b = a.isValid("({})")
print(b)

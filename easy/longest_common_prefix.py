class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        common_prefix = ""
        i = 0
        length = len(strs)
        while i < len(strs[0]):
            if strs[0][i] == strs[length - 1][i]: # c == c
                common_prefix += strs[0][i]
            else:
                break
            i += 1
        return common_prefix
    
# It firts sorts the list, that way you can have shorter words first, which will then limit the size of the loop 
# for what could possibly be the maximum prefix. 
# After that we compare letters from the first and last words of the sorted list. 
# When they match, we append the matched chars in common_prefix variable.
# When they differ, we know we have exausted the possibility of matching prefixes, returning the final common_prefix. 
# It's a good solution, however, won't work for all cases
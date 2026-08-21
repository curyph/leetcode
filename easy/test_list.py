class Solution:
    current_value = None
    def romanToInt(self, s: str) -> int:
        values_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        char_dict = {}
        num = 0
        # for ch in s:            
        #     if not ch in values_dict:
        #         raise Exception("Invalid Char")
                
        #     num += values_dict[ch]
        # return num
        for i in range(len(s)):
            if i + 1 < len(s):
                current_value = s[i]
                next_value = s[i + 1]
                val = self.check_next(current_value, next_value)
                if not val:
                    num += values_dict[s[i]]                    
                else:
                    num += val
            else: 
                num += values_dict[s[i]]

        print(num)                  

    def check_next(self, current_value, next_value):
            # current_value = s[i]
            # next_value = s[i + 1]
            if current_value == "I" and next_value == "V":
                return 4
            elif current_value == "I" and next_value == "X":
                return 9
            elif current_value == "X" == next_value == "L":
                return 40
            elif current_value == "X" == next_value == "C":
                return 90
            elif current_value == "C" == next_value == "D":
                return 400
            elif current_value == "C" == next_value == "M":
                return 900
            return None
        
a = Solution()
a.romanToInt("IV")

# PEDRO
class Solution:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if not i == j:
                    if nums[j] + nums[i] == target:
                        nums_list = [i, j]                        
                        return nums_list
 

# BEST RANKED
class Solution_2:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], index]

            seen[number] = index
        print(seen)
            
# SINGLE PASS HASH TABLE PEDRO
class Solution_2:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        sum_dct = {}
        
        # map inside the dict all the values and their indexes in key:value (value:index)
        # when target - current_val = some element inside the dict, we know we have achieved the two number sum 
        
        # dentro do meu dicionário eu preciso ter valor:índice
        # caso a diferença entre target e o número atual do loop seja igual um elemento do dict
        # retorna o value do dict com o seu valor + o i atual em uma lista
        num_length = len(nums)
        
        for i in range(num_length):
            current_sum = target - nums[i]
            
            if current_sum in sum_dct:
                return [sum_dct[current_sum], i]
            sum_dct[nums[i]] = i
        return []
            
result = Solution_2.twoSum([2,17,50,25,39,44, 93, 3], 5)
print(result)
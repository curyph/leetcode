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
            
            
result = Solution_2.twoSum([2,17,50,25,39,44, 93, 3], 5)
print(result)
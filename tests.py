class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
     
        # CLASSIC BRUTEFORCE
        # right = len(nums)        
        # for i in range(right):
        #     for j in range(right):
        #         if i != j:
        #             pair_sum = nums[i] + nums[j]
        #             if pair_sum == target:
        #                 return [i, j]            
        # return []
    
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found



# a = Solution()
# nums = [3,2,4]
# target = 6
# b = a.twoSum(nums, target)

# print(b)

a = [1, 2, 3, 4, 5]
ll = len(a)
print(ll)

for i in range(1, 5):
    print(i)

# RIDICULOUS ALGORITHM
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:        
        left = 0
        right = 1
        nums_size = len(nums)        
        if target <= nums[0]:
            return 0
        if target > nums[nums_size - 1]:
            return nums_size        
        while right < nums_size:
            if target == nums[left]:
                return left
            if target > nums[left] and target <= nums[right]:
                return right
            left += 1
            right += 1
                
# CLASSIC BINARY SEARCH

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:   
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
            
        return left
            
                     
        
            
a = Solution()
#b = a.searchInsert([1], 2)
b = a.searchInsert([1,3,5,6], 7)
print(b)
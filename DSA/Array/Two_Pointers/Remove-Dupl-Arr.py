class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        
        for n in nums:
            if k < 2 or n != nums[k - 2]:
                nums[k] = n
                k += 1
                
        return k

nums = [1,1,1,2,2,3]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)
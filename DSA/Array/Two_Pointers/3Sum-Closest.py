class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Optimization: Skip duplicate values for the 'i' pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if this current_sum is nearer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers to try and get closer to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

nums = [-1,2,1,-4]
target = 1
solution = Solution()
result = solution.threeSumClosest(nums, target)
print(result)
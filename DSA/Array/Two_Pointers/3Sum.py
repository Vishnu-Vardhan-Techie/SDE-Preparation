class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                three_sum = value + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

nums = [-1,0,1,2,-1,-4]
solution = Solution()
result = solution.threeSum(nums)
print(result)


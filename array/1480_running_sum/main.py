class Solution:
    def runningSum(self, nums):
        # Viết solution ở đây
        current_sum = 0
        results = []
        for num in nums:
            current_sum += num 
            results.append(current_sum)
        return results                        
solution = Solution()
# for num in nums:
#     print(num)
nums = [1, 2, 3, 4]
result = solution.runningSum(nums)

print(result)
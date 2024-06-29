from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        
        i = 0
        while i <= n - 3:
            if nums[i] == 0:
                # Flip the triplet starting at index i
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1
                # After flipping, check the current triplet again
                i -= 2 if i >= 2 else 0
            else:
                i += 1
        
        # After processing, check for any remaining zeros
        if any(num == 0 for num in nums):
            return -1
        
        return operations
    
example_1st = [0,1,1,1,0,0] # 3
example_2nd = [0,1,1,1] # -1
example_3rd = [1,0,0,1,1,1,0,0,1]

solution = Solution()
a1 = solution.minimumOperations(example_1st)
a2 = solution.minimumOperations(example_2nd)
a3 = solution.minimumOperations(example_3rd)

print(f'1st input: {example_1st}, 1st answer: {a1}')
print(f'2nd input: {example_2nd}, 2nd answer: {a2}')
print(f'3rd input: {example_3rd}, 3rd answer: {a3}')
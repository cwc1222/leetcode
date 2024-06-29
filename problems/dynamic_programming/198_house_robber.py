'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security systems connected 
and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

-----------------------------------------------------------------------------------
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

-----------------------------------------------------------------------------------
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

-----------------------------------------------------------------------------------
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

from typing import List

memo = []

def rob(nums: List[int], i: int) -> int:
    if (i < 0):
        return 0
    if memo[i] is not None:
        return memo[i]
    memo[i] = max(rob(nums, i - 2) + nums[i], rob(nums, i - 1))
    return memo[i]

class Solution:
    def rob(self, nums: List[int]) -> int:
        global memo
        memo = [None for _ in nums]
        return rob(nums, len(nums) - 1)

s = Solution()
input_1 = [1,2,3,1]
input_2 = [2,7,9,3,1]
input_3 = [2,1,1,2]
input_4 = [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
a1 = s.rob(input_1)
a2 = s.rob(input_2)
a3 = s.rob(input_3)
a4 = s.rob(input_4)

print(f"input {input_1}, answer {a1}")
print(f"input {input_2}, answer {a2}")
print(f"input {input_3}, answer {a3}")
print(f"input {input_4}, answer {a4}")

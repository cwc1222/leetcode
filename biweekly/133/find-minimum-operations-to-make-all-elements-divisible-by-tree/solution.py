from typing import List

def find_min_op(num: int):
    if num % 3 == 0 :
        return 0
    added = 0
    substracted = 0
    for i in range(1, 51):
        if (num + i) % 3 == 0:
            added = i
            break
    for i in range(1, 51):
        if (num - i) % 3 == 0:
            substracted = i
            break
    return min(added, substracted)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_ops = 0
        for num in nums:
            min_ops += find_min_op(num)
        return min_ops

example_1st = [1,2,3,4] # 3
example_2nd = [3,6,9] # 0
example_3rd = [4,10,10] # 1

solution = Solution()
a1 = solution.minimumOperations(example_1st)
a2 = solution.minimumOperations(example_2nd)
a3 = solution.minimumOperations(example_3rd)

print(f'1st input: {example_1st}, 1st answer: {a1}')
print(f'2nd input: {example_2nd}, 2nd answer: {a2}')
print(f'3rd input: {example_3rd}, 3rd answer: {a3}')

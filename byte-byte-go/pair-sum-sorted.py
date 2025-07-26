from typing import List

nums = [-1, 2, 4, 5, 6, 10, 14, 18]
target = 9

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left, right]
    return []


result = pair_sum_sorted(nums, target)
print(result)
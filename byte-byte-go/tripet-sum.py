from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()

    for i in range(len(nums)):
        # the 'a' value will never be larger than 0 becuase that implies all proceeding values are positive
        if nums[i] > 0:
            break
        # here we want to continue on if the next value is the same as the previous
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # pass in the array, the start value, and the target
        # the target for this is the -(nums - 1)
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets 

def pair_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[int]:
    pairs = []
    left, right = start, len(nums) -1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            if left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs



from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()

    for i in range(len(nums)):
        # triplets consiting of only positive number will never be sum to 0
        if nums[i] > 0:
            break
        # to avoid duplicate triplets, skip 'a' if its the same as the previous number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # find all pairs that sum to a target of '-a' (-nums[i])
        pairs = pair_sum_sorted_all_pairs(nums, i + 1, -nums[1])
        for pair in pairs:
            triplets.append([nums[i]] + pair)

    return triplets

















def pair_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[int]:
    pairs = []
    left, right = start, len(nums) - 1 

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            # stuff
            pairs.append([nums[left], nums[right]])
            left += 1
            # to avoid duplicate [b, c] pairs, skip b if its the same as the previous
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    return pairs


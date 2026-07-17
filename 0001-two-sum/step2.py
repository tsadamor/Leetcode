class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index: dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[num] = i

        raise ValueError("can't find the solution")

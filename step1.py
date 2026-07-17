from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

        return []


def main() -> None:
    nums = [3, 2, 4]
    target = 6
    Solver = Solution()
    res = Solver.twoSum(nums, target)
    print(res)


if __name__ == "__main__":
    main()

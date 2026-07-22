class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        end_of_nonzeroes = 0

        for i, num in enumerate(nums):
            if num == 0:
                continue

            nums[end_of_nonzeroes], nums[i] = nums[i], nums[end_of_nonzeroes]
            end_of_nonzeroes += 1


def main() -> None:
    Solver = Solution()
    nums = [0,1,0,3,12]
    print(f"before: {nums}")
    Solver.moveZeroes(nums)
    print(f"after: {nums}")


if __name__ == "__main__":
    main()
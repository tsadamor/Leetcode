class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        end_of_nonzeroes = 0

        while i < len(nums):
            if nums[i] != 0:
                tmp = nums[end_of_nonzeroes]
                nums[end_of_nonzeroes] = nums[i]
                nums[i] = tmp
                
                end_of_nonzeroes += 1
            i += 1


def main() -> None:
    Solver = Solution()
    nums = [0,1,0,3,12]
    print(f"before: {nums}")
    Solver.moveZeroes(nums)
    print(f"after: {nums}")


if __name__ == "__main__":
    main()

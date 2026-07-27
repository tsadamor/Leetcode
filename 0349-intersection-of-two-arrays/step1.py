class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = []
        for num in nums1_set:
            if num in nums2_set:
                res.append(num)

        return res


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_seen = {}
        res = []

        for num in nums1:
            num_to_seen[num] = 1

        for num in nums2:
            if num_to_seen.get(num) = 1:
                res.append(num)
                num_to_seen[num] += 1

        return res
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # returns an arbitrary `i` from such that `arr[i-1] <= value <= arr[i]` and `low <= i <= high`
        def insertion_point(arr: List[int], val: int, low: int, high: int) -> int:
            if low == high:
                return low

            mid = (low + high) // 2

            if val == arr[mid]:
                return mid
            elif val < arr[mid]:
                return insertion_point(arr, val, low, mid)
            else:
                return insertion_point(arr, val, mid + 1, high)


        # (build[i] == x && i < lis) implies that there exist a subsequence in `nums` ending in value `x` of length `i + 1`
        build = [999999999] * len(nums)

        lis = 0
        for n in nums:
            ip = insertion_point(build, n, 0, lis + 1)
            build[ip] = n
            lis = max(lis, ip + 1)

        return lis
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = nums1+nums2
        arr.sort()
        mid_val = abs((len(arr)/2))

        if len(arr) == 2:
            return sum(arr)/2
        if len(arr) % 2 != 0:
            return (float(arr[int(mid_val)]))
        else:
            val = (arr[int(mid_val)] + arr[int(mid_val-1)])/2
            return float(val)

if __name__ == "__main__":
    sln = Solution()
    nums1 = []
    nums2 = [2,3]
    print(sln.findMedianSortedArrays(nums1, nums2))
class Solution:
    def maxArea(self, height) -> int:
        out = 0 
        j = len(height)-1
        i=0
        while i <j:
            out = max(out, 
                    min(height[i], height[j]) * (j-i)
            )
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return out
if __name__ == "__main__":
    sln = Solution()
    arr  = [2,3,4,5,18,17,6]
    print(sln.maxArea(arr))
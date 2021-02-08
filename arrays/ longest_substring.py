class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        out = []
        for i, j in zip(s, s[1:]):
            if i != j :
                out.append(i)
                out.append(j)
                print(i,j)

        return len(out)
        


if __name__ == "__main__":
    sln = Solution()
    s = "abcabcbb"
    print(sln.lengthOfLongestSubstring(s))
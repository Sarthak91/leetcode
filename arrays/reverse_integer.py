class Solution:
    def reverse(self, x: int) -> int:
        sign = None
        
        if x < 0:
            sign = -1
        else:
            sign = 1
        out = 0
        while x != 0:
            x = abs(x)
            rem = x % 10
            out  = out * 10 +  rem                        
            print(out)
            x = int(x / 10)
        if  out > int(2**31 - 1) & out < int(2**31 - 1):
            out = 0
        return sign * out

if __name__ == "__main__":
    sln = Solution()
    x = 1534236469
    print(sln.reverse(x))

        
        
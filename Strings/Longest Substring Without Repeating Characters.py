class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        look_up = {}
        start = 0
        maxlen = 0
        i = 0
        while(i<len(s)):
            
            if s[i] in look_up:
                indx = look_up[s[i]]
                if indx >= start:
                    start = indx+1
            
            
            look_up[s[i]] = i
            maxlen = max(maxlen,i-start+1)
            print(maxlen)
            i += 1
        
        return maxlen
                
                
            
        
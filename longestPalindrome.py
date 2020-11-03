class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        st = set()
        count =  0
        for i in s:
            if i not in st:
                st.add(i)
            else:
                st.remove(i)
                count += 2
        
        if len(st) > 0:
            count  +=1
            
        return count
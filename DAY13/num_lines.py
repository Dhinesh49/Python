class Solution(object):
    def numberOfLines(self, widths, s):
        line = 1
        current_width = 0
        for c in s:
            if current_width + widths[ord(c)-ord('a')] <= 100:
                current_width+=widths[ord(c)-ord('a')]
            else:
                line+=1
                current_width = widths[ord(c)-ord('a')]
        return [line, current_width]



        

        
        

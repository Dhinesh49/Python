class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(string): 
            stack = []
            for c in string: 
                if c == "#": 
                    if stack: 
                        stack.pop()
                else: 
                    stack.append(c)
            
            return "".join(stack)

        return check(s) == check(t)

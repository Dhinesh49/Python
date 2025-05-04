class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # two pointers
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # skip right
                sr = r - 1
                l_c = l
                while (l_c < sr):
                    if s[l_c] != s[sr]: # keep going
                        break
                    l_c += 1
                    sr -= 1
                if l_c >= sr: # return True if loop wasnt broken (no mismatch)
                    return True

                # skip left
                sl = l + 1
                r_c = r
                while (sl < r_c):
                    if s[sl] != s[r_c]:
                        break
                    sl += 1
                    r_c -= 1
                if sl >= r_c: # return True if loop wasnt broken (no mismatch)
                    return True
                    
                return False # neither loops worked
            l += 1
            r -= 1

        return True

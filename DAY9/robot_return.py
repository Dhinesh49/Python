class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('L') != moves.count('R'):
            return False
        elif moves.count('U') != moves.count('D'):
            return False
        else:
            return True

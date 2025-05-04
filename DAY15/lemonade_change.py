class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        fives = tens = 0

        for b in bills:

            if b == 5:   # take it
                fives += 1
            if b == 10:  # take it and give change
                tens +=1
                fives -=1
            if b == 20:  # take it and give change
                if tens > 0:
                    tens -=1
                    fives -=1
                else:
                    fives -=3
            if fives < 0 or tens < 0:
                return False
 
        return True

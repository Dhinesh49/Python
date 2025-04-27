class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row_set1 = set("qwertyuiopQWERTYUIOP")
        row_set2 = set("asdfghjklASDFGHJKL")
        row_set3 = set("zxcvbnmZXCVBNM")
        answer = []

        for word in words:
            
            if word[0] in row_set1:
                for letter in word:
                    if letter not in row_set1:
                        break
                else: answer.append(word)
            elif word[0] in row_set2:
                for letter in word:
                    if letter not in row_set2:
                        break
                else: answer.append(word)
            elif word[0] in row_set3:
                for letter in word:
                    if letter not in row_set3:
                        break
                else: answer.append(word)
        
        return answer
            

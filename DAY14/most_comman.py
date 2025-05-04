import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\w+', paragraph.lower())
        word_count = defaultdict(int)
        for word in words:
            if word not in banned:
                word_count[word]+=1
        
        return max(word_count, key= word_count.get) 
        
        

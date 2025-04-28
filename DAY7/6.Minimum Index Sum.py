class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        commonString = {}

        # nadji zajednicki
        for item1 in list1:
            if item1 in list2:
                index1 = list1.index(item1)
                
                index2 = list2.index(item1)
                
                sum = index1 + index2
                
                commonString[item1] = sum


        
        leastSum = commonString.get(min(commonString,key=commonString.get))

        print(leastSum)


        result = []

        for key, value in commonString.items():
            if leastSum == value:
                result.append(key)
                
                
        return result
        

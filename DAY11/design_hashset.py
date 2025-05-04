class MyHashSet(object):

    def __init__(self):
        self.list=[]
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key) ==False:
            self.list.append(key)
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.list.remove(key)
        else:
            pass
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """

        if key in self.list:
            return True
        return False

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Time O(n)
# Space O(n)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenList = []
        self.flatten(nestedList)
        self.iterator = iter(self.flattenList)
        self.nextVal = None
    
    def flatten(self, nestedList: [NestedInteger]):
        for nestedInt in nestedList:
            if nestedInt.isInteger():
                self.flattenList.append(nestedInt.getInteger())
            else:
                self.flatten(nestedInt.getList())

    def next(self) -> int:
        return self.nextVal
    
    def hasNext(self) -> bool:
        try:
            self.nextVal = next(self.iterator)
            return True
        except StopIteration:
            self.nextVal = None
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
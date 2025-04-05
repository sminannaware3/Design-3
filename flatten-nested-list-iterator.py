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

# Time O(1)
# Space O(h)
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [iter(nestedList)]
        self.iterator = None 
        self.nextVal = None

    def next(self) -> int: # O(1)
        return self.nextVal.getInteger() 
    
    def hasNext(self) -> bool: # Time O(h) max depth of nesting; amortized O(1)
        while len(self.stack) > 0: # This while is important to build stack when there are nested lists, while only exists when it finds int value
            try:
                self.nextVal = next(self.stack[-1])
                if self.nextVal.isInteger():
                    return True
                else:
                    self.stack.append(iter(self.nextVal.getList()))
            except StopIteration:
                self.nextVal = None
                self.stack.pop()
        return False

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
# Time O(n)
# Space O(n) cache space
class LRUCache:
    class TreeNode:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.currCap = 0
        
    def removeTail(self) -> None: #O(1)
        # temp = self.tail
        if self.currCap > 1:
            if self.tail != None:
                self.tail = self.tail.prev
                if self.tail != None:
                    self.tail.next = None
                self.currCap -= 1
        else: 
            self.tail = None
            self.head = None

    def search(self, key: int) -> TreeNode: #O(n)
        curr = self.head
        while curr != None:
            if curr.key == key: break
            curr = curr.next
        return curr

    def get(self, key: int) -> int: #O(n)
        # 4 cases : if ele is tail, middle, head, and not found
        node = self.search(key)
        if node == None: return -1
        # if head == node do nothing
        if node == self.head: return node.val
        self.moveToHead(node)
        return node.val

    def moveToHead(self, node: TreeNode) -> None: # O(1)
        if self.tail == node: 
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next != None: node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node

    def put(self, key: int, value: int) -> None: #O(n)
        node = self.search(key)
        if node != None:
            node.val = value
            if node != self.head: self.moveToHead(node)
            return
        if self.currCap == self.capacity:
            self.removeTail()
        newEle = self.TreeNode(key, value)

        if self.head != None: self.head.prev = newEle
        newEle.next = self.head
        newEle.prev = None
        self.head = newEle

        if self.tail == None: self.tail = newEle

        self.currCap += 1

# Time O(1)
# Space O(2n) cache space + map
class LRUCache:
    class TreeNode:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.currCap = 0
        self.nodemap = {}
        
    def removeTail(self) -> None: #O(1)
        # temp = self.tail
        del self.nodemap[self.tail.key]
        if self.currCap > 1:
            if self.tail != None:
                self.tail = self.tail.prev
                if self.tail != None:
                    self.tail.next = None
        else: 
            self.tail = None
            self.head = None
        self.currCap -= 1

    def search(self, key: int) -> TreeNode: #O(1) space O(n)
        if key in self.nodemap:
            return self.nodemap[key]
        else: return None

    def get(self, key: int) -> int: #O(1)
        # 4 cases : if ele is tail, middle, head, and not found
        node = self.search(key)
        if node == None: return -1
        # if head == node do nothing
        if node == self.head: return node.val
        self.moveToHead(node)
        return node.val

    def moveToHead(self, node: TreeNode) -> None: #O(1)
        if self.tail == node: 
            self.tail = self.tail.prev
        node.prev.next = node.next
        if node.next != None: node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node

    def put(self, key: int, value: int) -> None: #O(1)
        node = self.search(key)
        if node != None:
            node.val = value
            if node != self.head: self.moveToHead(node)
            return
        if self.currCap == self.capacity:
            self.removeTail()
        newEle = self.TreeNode(key, value)
        self.nodemap[key] = newEle

        if self.head != None: self.head.prev = newEle
        newEle.next = self.head
        newEle.prev = None
        self.head = newEle

        if self.tail == None: self.tail = newEle

        self.currCap += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
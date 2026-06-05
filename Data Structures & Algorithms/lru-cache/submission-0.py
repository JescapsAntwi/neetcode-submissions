class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev = self.next = None #initialize the two pointers 

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} #map key to node 

        #left = LRU, right= most recent 
        #before we have any value in our cache we need a couple of dummy pointers to tell us the most recent and least recent cache 
        self.left, self.right = Node(0, 0), Node(0, 0)
        #we want the two nodes to be connected to each other because when we put a new node we put them in the middle of these two 
        self.left.next, self.right.prev = self.right, self.left 

    #helper functions to help with updating most recent 
    #remove node from list 
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 

    #insert node at right 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next  = nxt.prev = node 
        node.next, node.prev = nxt, prev 
    

    def get(self, key: int) -> int:
        if key in self.cache:
            #remove and insert at the right so it becomes the most recent used cache
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) #insert into linked list 

        if len(self.cache) > self.cap:
            #remove from this list and delete the LRU from the cache or hashmap 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


        
 
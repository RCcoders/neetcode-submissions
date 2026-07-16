class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # Least Recently Used (LRU)
        self.right = Node(0, 0)  # Most Recently Used (MRU)

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert a node before the right dummy node (MRU position)
    def insert(self, node: Node) -> None:
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU position
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)
        self.cache[key] = node

        # Insert at MRU position
        self.insert(node)

        # Remove LRU node if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        if not (isinstance(key, int) and isinstance(val, int) and (isinstance(left, TreeNode) or not left)
                and isinstance(right, TreeNode) or not right):
            raise TypeError
        self.key = key
        self.price = val
        self.leftChild = left
        self.rightChild = right


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def put(self, key, val):
        if not (isinstance(key, int) and isinstance(val, int)):
            raise TypeError
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.leftChild:
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val)
        elif key > current_node.key:
            if current_node.rightChild:
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val)

    def get(self, key):
        if not key.isdigit():
            raise TypeError
        key = int(key)
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.price
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)


try:
    obj = BinarySearchTree()
    for i in range(5):
        obj.put(i, i)
    print("Cost:", obj.get(input("Product code: ")) * int(input("Number of products: ")))

except TypeError:
    print("TypeError!")

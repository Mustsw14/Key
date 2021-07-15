class BinaryTreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.parent = None
        self._left_child = left_child
        self._right_child = right_child
        if left_child:
            left_child.parent = self
        if right_child:
            right_child.parent = self

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child




class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    def __iter__(self):
        return self

    def __next__(self):
        def inorder(root):
            if root:
                inorder(root.left_child)
                print(root.value)
                inorder(root.right.child)
            inorder(self.root)
            return self

class PreOrderIterator():
    def __init__(self,root):
       self.root = root

    def __iter__(self):
        return self

    def __next__(self):
       def preorder(root):
           if root:
               print(root.value)
               preorder(root.left.child)
               preorder(root.right.child)
       preorder(self.root)


class PostOrderIterator():
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return self

    def __next__(self):
        def postorder(root):
            if root:
                postorder(root.left.child)
                postorder(root.right.child)
                print(root.value)
        postorder(self.root)


class InOrderIterator():
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return self

    def __next__(self):
        def inorder(root):
            if root:
                inorder(root.left.child)
                print(root.value)
                inorder(root.right.child)
        inorder(self.root)


# sample
if __name__ == '__main__':
    n1 = BinaryTreeNode("A")
    n2 = BinaryTreeNode("B")
    n3 = BinaryTreeNode("C", n1, n2)
    n4 = BinaryTreeNode("D")
    n5 = BinaryTreeNode("E", n4, n3)
    n6 = BinaryTreeNode("F", n5)
    n7 = BinaryTreeNode("G")
    n8 = BinaryTreeNode("H", n6, n7)
    tree = BinaryTree(n8)
    #print(tree.root.value)
    #print(tree.root.left_child.left_child.value)
    it = iter(tree)
    next(it)

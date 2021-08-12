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
        return InOrderIterator.printinorder(self._root)


class PostOrderIterator:

    def printPreOrder(node):
        lst =[]
        node1 = node
        while node.value not in lst:
            if node1.value not in lst:
                while node1.left_child != None:
                    node1 = node1.left_child
                    node1_value = node1.value
                lst.append(node1.value)
            else:
                if node1.parent.right_child != None and node1.parent.right_child.value  not in lst:
                    node1 = node1.parent.right_child
                    while node1.left_child != None:
                        node1 = node1.left_child
                    lst.append(node1.value)
                if node1.parent.right_child == None or node1.parent.right_child.value in lst:
                    node1 = node1.parent
                    lst.append(node1.value)
        for items in lst:
            print(items)

class InOrderIterator:
    #Left,Visit,Right
    def printinorder(node):
        lst =[]
        node1 = node
        while node.value not in lst:
            if node1.value not in lst:
                while node1.left_child != None:
                    node1 = node1.left_child
                    node1_value = node1.value
                lst.append(node1.value)
            else:
                if node1.parent.left_child == None or node1.parent.left_child.value in lst:
                    node1 = node1.parent
                    while node1.value in lst:
                        node1 = node1.parent
                    lst.append(node1.value)
                if node1.right_child  != None and node1.right_child.value not in lst:
                    node1 = node1.right_child
                    while node1.left_child != None:
                        node1 = node1.left_child
                    lst.append(node1.value)
        for items in lst:
            print(items)

class PreOrderIterator:
    def printpreorder(node):
        lst =[]
        node1 = node
        node2 = node
        while node2.left_child != None:
            node2 = node2.right_child
        while node2.value not in lst:
            if node1.value not in lst:
                lst.append(node1.value)
            else:
                if node1.left_child.value not in lst:
                        while node1.left_child != None:
                            node1 = node1.left_child
                            lst.append(node1.value)
                #if node1.left_child == None:
                        #break
                if node1.right_child !=None:
                        node1 = node1.right_child
                        lst.append(node1.value)


                if node1.parent.right_child != None:
                    if node1.parent.right_child.value not in lst:
                        node1 = node1.parent.right_child
                        lst.append(node1.value)

                if node1.right_child == None and node1.left_child == None:
                    if node1.value == node.value:
                        break
                    else:
                        while node1.parent.value in lst:
                            node1 = node1.parent
                            if node1.value == node.value:
                                break




        for items in lst:
            print(items)








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
    #PST1 = PostOrderIterator
    #PST1.printPreOrde(tree.root)
    #IST1 = InOrderIterator
    #IST1.printinorder(tree.root)
    #RST1 = PreOrderIterator
    #RST1.printpreorder(tree.root)
    tree.__iter__()



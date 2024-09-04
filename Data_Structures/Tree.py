# Key Concepts
    # Node: The fundamental unit of a tree, which stores data and has pointers to child nodes.
    # Root: The topmost node in the tree, from which all nodes descend.
    # Parent: A node that has one or more child nodes.
    # Child: A node that descends from another node (its parent).
    # Leaf: A node that has no children (it's at the end of a branch).
    # Subtree: A portion of the tree that includes a node and its descendants.
    # Height: The length of the longest path from a node to a leaf.
    # Depth: The length of the path from the root to a particular node.


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class TreeNode:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None
    
    def insert(self, value):
        #If the tree is empty
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
    


    # Insertion operation
    def insert_recursive(self, root, value):
        #if Value is is less than root, then it goes to left side
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.insert_recursive(root.left, value)

        # If value is greater that root, then it goes to right side        
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self.insert_recursive(root.right, value)
    


    #Start from the leaf of the right, node, right
    def inorder_traversal(self):
        return self.inorder_traversal_recursive(self.root, result=[])

    def inorder_traversal_recursive(self, root, result=[]):
        if root:
            self.inorder_traversal_recursive(root.left, result)
            result.append(root.value)
            self.inorder_traversal_recursive(root.right, result)
        return result

    

    #Start root, left, right
    def preorder_traversal(self):
        return self.preorder_traversal_recursive(self.root, result=[])
    
    def preorder_traversal_recursive(self, root, result=[]):
        if root:
            result.append(root.value)
            self.preorder_traversal_recursive(root.left, result)
            self.preorder_traversal_recursive(root.right, result)
        return result
    

    #Post Order = left => right => root
    def postorder_traversal(self):
        return self.postorder_recursive(self.root, result=[])

    def postorder_recursive(self, root, result=[]):
        if root:
            self.postorder_recursive(root.left, result)
            self.postorder_recursive(root.right, result)
            result.append(root.value)
        return result
    
    #Lets Implement Search Recursively
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, root, value):
        if root is None:
            return False
        
        if root.value == value:
            return True
        elif value < root.value:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)
    

Tree = TreeNode()
print(Tree.isEmpty())
Tree.insert(5)
Tree.insert(4)
Tree.insert(3)
Tree.insert(6)
Tree.insert(7)
Tree.insert(8)
Tree.insert(1)
print(Tree.inorder_traversal())
print(Tree.preorder_traversal())
print(Tree.postorder_traversal())
print(Tree.isEmpty())
print(Tree.search(8))
print(Tree.search(10))
# Inorder Traversal: [1, 3, 4, 5, 6, 7, 8]
# [5, 4, 3, 1, 6, 7, 8]

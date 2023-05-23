# class Node:
#     def __init__(self) -> None:
#         pass

class BSTree:
    """
        class for binary tree DS
    """
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        """
            constructor
        """
        self.val =val
        self.left = left
        self.right = right

    def insert_node(self, val:int)-> None:
        # fmt: off
        """
            description:    populates trees with individual nodes
            val:            value to be inserted
            returns:        None
        """
        # fmt: on

        if self.val:
            if val <=self.val:
                if self.left is None:
                    self.left = BSTree(val)
                else:
                    self.left.insert_node(val)
            else:
                if self.right is None:
                    self.right = BSTree(val)
                else:
                    self.right.insert_node(val)
        else:
            self.val=val

    def inorderTraversal(self, root=None)->str[int]:
        """
            description:    inorder Traversal of BTree
            root:           current node of the tree
            returns:        return the list of values in Tree inorder
        """
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []
    
    def preorderTraversal(self, root =None)->str[int]:
        """
            description:    preorder Traversal of BTree
            root:           current node of the tree
            returns:        return the list of values in Tree preorder
        """
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []
    
    def postorderTraversal(self, root =None)->str[int]:
        """
            description:    postorder Traversal of BTree
            root:           current node of the tree
            returns:        return the list of values in Tree postorder
        """
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []
    
    def check_height(self,root)->int:
        # fmt: off
        """
            description:    checks the height/depth of the tree
            root:           node of the tree to find height
            returns:        height in integer
        """
        # fmt: on

        if root == None:
            return 0
        return 1 + max(self.check_height(root.left), self.check_height(root.right))

    def search(self, root, val:int)->int:
        # fmt: off
        """
            description:    search for a value within the tree and return a bool
            val:            value to search for
            return:         True when it exist, otherwise False
        """
        # fmt: on

        if root == None:
            return False

        if root.val == val:
            return True
        
        return self.search(root.left, val) or self.search(root.right,val)

    def sum_of_all_values(self, root)-> int:
        # fmt: off
        """
            description:    Summation of all values in the tree
            root:           tree to search
            return:         integer sum
        """
        # fmt: on

        if root is None:
            return 0
        
        return root.val + self.sum_of_all_values(root.left) + self.sum_of_all_values(root.right)
    
    def maximum(self, root)->int:
        # fmt: off
        """
            description:    Find maximum value in the tree
            root:           tree to search
            return:         maximum value in int
        """
        # fmt: on

        # if not sorted
        # if root is None:
        #     return 0
        
        # return max(root.val, max(self.maximum(root.left), self.maximum(root.right)))

        if root.right is None:
            return root.val

        return self.maximum(root.right)

    def find_all_values_at_distance_k_from_node(self, root, val)->int:
        # fmt: off
        """
            description:    Find all values at distance k from node
            root:           tree to search
            return:         none if no said node in tree or all values that are distance k from node
        """
        # fmt: on
        if not self.search(root,val):
            return None

        # more work needed

    def avl_insert_node(self, root, val)->None:
        pass

if __name__ == "__main__":
    t = BSTree()
    t.insert_node(3)
    t.insert_node(5)
    t.insert_node(4)
    t.insert_node(2)
    t.insert_node(1)
    t.insert_node(10)
    t.insert_node(11)
    print(t.find_all_values_at_distance_k_from_node(t, 12))



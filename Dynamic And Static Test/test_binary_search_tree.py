import unittest
from binary_search_tree_recursive import BinarySearchTree, Node


class TestMetamorphicRelations(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mr1_insertion_with_properties(self):
        print("\n--- MR1: Insertion with Tree Properties, Traversals, and Existence Check ---")

        # Test Group 1: Basic Insertion with Existence and Traversal Checks
        values = [15, 10, 25]
        for value in values:
            self.bst.put(value)
        
        # Max and Min Labels
        print("Max label after insertion:", self.bst.get_max_label())
        print("Min label after insertion:", self.bst.get_min_label())
        
        # Traversals
        print("In-order traversal:", [i.label for i in self.bst.inorder_traversal()])
        print("Pre-order traversal:", [i.label for i in self.bst.preorder_traversal()])
        
        # Existence Checks
        print("Checking existence of 10, 15, 25, and 20:")
        print("10 exists:", self.bst.exists(10))
        print("15 exists:", self.bst.exists(15))
        print("25 exists:", self.bst.exists(25))
        print("20 exists:", self.bst.exists(20))

        # Follow-up Input
        follow_up_values = [5, 20, 30]
        for value in follow_up_values:
            self.bst.put(value)

        # Max and Min Labels after follow-up insertion
        print("Max label after follow-up insertion:", self.bst.get_max_label())
        print("Min label after follow-up insertion:", self.bst.get_min_label())

        # Traversals after follow-up insertion
        print("In-order traversal after follow-up:", [i.label for i in self.bst.inorder_traversal()])
        print("Pre-order traversal after follow-up:", [i.label for i in self.bst.preorder_traversal()])

        # Existence Checks after follow-up insertion
        print("Checking existence of 5, 10, 15, 20, 25, 30:")
        print("5 exists:", self.bst.exists(5))
        print("10 exists:", self.bst.exists(10))
        print("15 exists:", self.bst.exists(15))
        print("20 exists:", self.bst.exists(20))
        print("25 exists:", self.bst.exists(25))
        print("30 exists:", self.bst.exists(30))


    def test_mr2_deletion_with_node_reassignment(self):
        print("\n--- MR2: Deletion with Node Reassignment, Traversals, and Existence Check ---")

        # Test Group 1: Deleting a Node with No Children
        values = [30, 20, 40]
        for value in values:
            self.bst.put(value)

        # Max and Min Labels before deletion
        print("Max label before deletion:", self.bst.get_max_label())
        print("Min label before deletion:", self.bst.get_min_label())

        # Traversals before deletion
        print("In-order traversal before deletion:", [i.label for i in self.bst.inorder_traversal()])
        print("Pre-order traversal before deletion:", [i.label for i in self.bst.preorder_traversal()])

        # Deleting node with no children
        print("\nDeleting node 40 (no children)")
        self.bst.remove(40)

        # Max and Min Labels after deletion
        print("Max label after deletion:", self.bst.get_max_label())
        print("Min label after deletion:", self.bst.get_min_label())

        # Traversals after deletion
        print("In-order traversal after deletion:", [i.label for i in self.bst.inorder_traversal()])
        print("Pre-order traversal after deletion:", [i.label for i in self.bst.preorder_traversal()])

        # Existence checks after deletion
        print("Checking existence of 20, 30, and 40:")
        print("20 exists:", self.bst.exists(20))
        print("30 exists:", self.bst.exists(30))
        print("40 exists:", self.bst.exists(40))




if __name__ == "__main__":
    unittest.main()

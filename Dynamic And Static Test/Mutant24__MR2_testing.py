import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation24MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation24_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 24: Deletion with Pre-Order Traversal Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(30)

        try:
            # Perform pre-order traversal after deletion (expecting a RecursionError due to the mutation)
            pre_order = [node.label for node in self.bst.preorder_traversal()]
            print(f"Pre-order traversal obtained after deletion: {pre_order}")
        except RecursionError as e:
            print("RecursionError encountered during pre-order traversal after deletion, which is expected due to Mutant 24.")
            self.fail(f"RecursionError encountered: {e}")

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation24MR2))

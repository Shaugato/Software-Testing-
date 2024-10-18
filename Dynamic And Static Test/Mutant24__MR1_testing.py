import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation24MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation24_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 24: Insertion with Pre-Order Traversal Verification ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        try:
            # Perform pre-order traversal (expecting a RecursionError due to the mutation)
            pre_order = [node.label for node in self.bst.preorder_traversal()]
            print(f"Pre-order traversal obtained: {pre_order}")
        except RecursionError as e:
            print("RecursionError encountered during pre-order traversal, which is expected due to Mutant 24.")
            self.fail(f"RecursionError encountered: {e}")

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation24MR1))

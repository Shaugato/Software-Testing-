import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation16MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation16_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 16: Deletion with Max Label Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(70)

        # Expected max label should be 80, but due to the mutation, it will return 30 (minimum value instead of maximum)
        try:
            max_label = self.bst.get_max_label()
            print(f"Max label obtained after deletion: {max_label}")
            expected_max_label = 80
            assert max_label == expected_max_label, f"Expected max label after deletion to be {expected_max_label}, but got {max_label}"
        except AssertionError as e:
            print(e)
            raise

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation16MR2))

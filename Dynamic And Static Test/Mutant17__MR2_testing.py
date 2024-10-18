import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation17MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation17_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 17: Deletion with Min Label Verification ---")

        # Insert values into BST
        values = [50, 30, 70, 10, 40, 60, 80]
        for value in values:
            self.bst.put(value)

        # Delete a node
        self.bst.remove(10)

        # Expected min label should be 30, but due to the mutation, it will return 80 (maximum value)
        try:
            min_label = self.bst.get_min_label()
            print(f"Min label obtained after deletion: {min_label}")
            expected_min_label = 30
            assert min_label == expected_min_label, f"Expected min label after deletion to be {expected_min_label}, but got {min_label}"
        except AssertionError as e:
            print(e)
            raise

# Running MR2 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation17MR2))

import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation17MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation17_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 17: Insertion with Min Label Verification ---")

        # Insert values into BST
        values = [20, 10, 30, 5, 25, 40]
        for value in values:
            self.bst.put(value)

        # Expected min label should be 5, but due to the mutation, it will return 40
        try:
            min_label = self.bst.get_min_label()
            print(f"Min label obtained: {min_label}")
            expected_min_label = 5
            assert min_label == expected_min_label, f"Expected min label to be {expected_min_label}, but got {min_label}"
        except AssertionError as e:
            print(e)
            raise

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation17MR1))

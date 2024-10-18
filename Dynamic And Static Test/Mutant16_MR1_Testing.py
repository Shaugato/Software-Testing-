import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation16MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation16_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 16: Insertion with Max Label Verification ---")

        # Insert values into BST
        values = [20, 10, 30, 25, 40]
        for value in values:
            self.bst.put(value)

        # Expected max label should be 40, but due to the mutation, it will return 10
        try:
            max_label = self.bst.get_max_label()
            print(f"Max label obtained: {max_label}")
            expected_max_label = 40
            assert max_label == expected_max_label, f"Expected max label to be {expected_max_label}, but got {max_label}"
        except AssertionError as e:
            print(e)
            raise

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation16MR1))

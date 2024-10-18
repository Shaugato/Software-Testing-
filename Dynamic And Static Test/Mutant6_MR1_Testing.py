import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation6MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation6_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 6: Insertion with Error Message Check ---")

        # Insert value into BST
        self.bst.put(10)
        try:
            self.bst.put(10)  # Inserting duplicate value
        except ValueError as e:
            error_message = str(e)
            print(f"Error encountered while inserting duplicate value: {error_message}")
            # Check if the error message contains the label
            expected_message = "Node with label 10 already exists"
            assert expected_message in error_message, f"Expected error message to contain label, but got: {error_message}"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation6MR1))

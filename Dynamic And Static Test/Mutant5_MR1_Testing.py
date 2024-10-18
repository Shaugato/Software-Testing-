import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation5MR1(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation5_mr1_insertion(self):
        print("\n--- Testing MR1 for Mutation 5: Insertion with Modified Comparison ---")

        # Insert values into BST
        values = [10, 5, 15, 5]  # Intentionally inserting a duplicate value (5)
        for value in values:
            try:
                self.bst.put(value)
                print(f"Inserted value {value}")
            except ValueError as e:
                print(f"Error encountered while inserting value {value}: {e}")

        # In-order traversal to check structure
        in_order = [i.label for i in self.bst.inorder_traversal()]
        expected_in_order = [5, 10, 15]  # Expect no duplicates
        assert in_order == expected_in_order, f"In-order traversal failed, got: {in_order}"

# Running MR1 Test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation5MR1))

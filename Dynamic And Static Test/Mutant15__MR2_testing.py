import unittest
from binary_search_tree_recursive import BinarySearchTree

class TestMutation15MR2(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_mutation15_mr2_deletion(self):
        print("\n--- Testing MR2 for Mutation 15: Deletion with Existence Check ---")

        # Insert values to form a tree
        values = [50, 30, 70, 60, 80]
        for value in values:
            self.bst.put(value)

        # Remove node 70, which has two children (60 and 80)
        self.bst.remove(70)

        # Verify that 70 no longer exists
        assert not self.bst.exists(70), "Node 70 should not exist after deletion"

        # Verify that other nodes still exist
        remaining_values = [50, 30, 60, 80]
        for value in remaining_values:
            exists = self.bst.exists(value)
            print(f"Checking existence of {value}: {exists}")
            assert exists, f"Node {value} should still exist but `exists()` returned {exists}"

# Running MR2 test
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMutation15MR2))

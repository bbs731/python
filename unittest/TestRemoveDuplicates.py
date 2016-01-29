import unittest
import duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def test_general_case(self):
        """
        Test remove shared where items appear in both lists.
        and items that appear in only one or the orther list
        shit holy
        """

        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = [2, 4, 5, 7]
        list_1_expected = [1, 3, 6]
        list_2_expected = [2, 4, 5, 7]

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)


if __name__ == '__main__':
    unittest.main(exit=False)
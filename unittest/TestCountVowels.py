import unittest
import countVowels


class TestCountVowels(unittest.TestCase):
    def test_example_1(self):
        """
        test count_lowercase_vowels with empty string
        """
        self.assertEqual(0, countVowels.count_lowercase_vowels(''))

    def test_example_2(self):
        """
        test count_lowercase_vowels with 'a'
        """
        self.assertEqual(1, countVowels.count_lowercase_vowels('a'))

    def test_example_3(self):
        """
        test count_lowercase_vowels with 'A'
        """
        self.assertEqual(0, countVowels.count_lowercase_vowels('A'))

    def test_example_4(self):
        """
        test count_loewrcase_vowels with 'b'
        """
        self.assertEqual(0, countVowels.count_lowercase_vowels('b'))

    def test_example_5(self):
        """
        test count_lowercase_vowels with 'pffffft'
        :return:
        """
        self.assertEqual(0, countVowels.count_lowercase_vowels('pffffft'))

    def test_example_6(self):
        """test count_lowercase_vowels with 'aeioua' """
        self.assertEqual(5, countVowels.count_lowercase_vowels('aeioua'))

if __name__ == '__main__':
    unittest.main(exit=False)
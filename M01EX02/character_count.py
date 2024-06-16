import unittest

def character_count(word):
    word = word.lower()  # Chuyển đổi tất cả thành chữ thường
    character_statistic = {}
    for i in word:
        if i in character_statistic:
            character_statistic[i] += 1
        else:
            character_statistic[i] = 1

    return character_statistic

class TestCharacterCount(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(character_count("Baby"), {'b': 2, 'a': 1, 'y': 1})

    def test_multiple_words(self):
        self.assertEqual(character_count("smiles"), {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1})

    def test_empty_string(self):
        self.assertEqual(character_count(""), {})

    def test_all_same_character(self):
        self.assertEqual(character_count("aaaa"), {'a': 4})

if __name__ == '__main__':
    unittest.main()

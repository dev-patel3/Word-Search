import unittest
from WordSearch import WordSearch
import random
import string
import time

class TestWordSearch(unittest.TestCase):
    def generate_grid(self, size):
        """Generate a square grid of random letters"""
        return ''.join(random.choice(string.ascii_lowercase) 
                      for _ in range(size * size))

    def generate_word(self, length):
        """Generate a random word of given length"""
        return ''.join(random.choice(string.ascii_lowercase) 
                      for _ in range(length))

    def test_small_grid_horizontal(self):
        """Test with a small grid where we know the answer"""
        grid = "abcde" + "fghij" + "klmno" + "pqrst" + "uvwxy"  # 5x5 grid
        ws = WordSearch(grid, ROW_LENGTH=5)  # Specify ROW_LENGTH=5 for 5x5 grid
        # Test known words
        self.assertTrue(ws.is_present("abc"))
        self.assertTrue(ws.is_present("fgh"))
        self.assertFalse(ws.is_present("xyz"))
        self.assertFalse(ws.is_present("aft"))  # vertical word, not allowed

    def test_small_grid_vertical(self):
        """Test vertical word finding"""
        grid = "abcde" + "fghij" + "klmno" + "pqrst" + "uvwxy"  # 5x5 grid
        ws = WordSearch(grid, ROW_LENGTH=5)
        self.assertTrue(ws.is_present("afkpu"))
        self.assertTrue(ws.is_present("bglqv"))
        self.assertFalse(ws.is_present("abfk"))  # partial match

    def test_edge_cases(self):
        """Test edge cases"""
        ROW_LENGTH = 10
        grid = self.generate_grid(ROW_LENGTH)  # 10x10 grid
        ws = WordSearch(grid, ROW_LENGTH=ROW_LENGTH)
        # Test empty word
        self.assertFalse(ws.is_present(""))
        # Test single character
        self.assertTrue(ws.is_present(grid[0]))
        # Test word longer than grid
        self.assertFalse(ws.is_present("a" * (ROW_LENGTH + 1)))

    def test_performance(self):
        """Test performance with large grid and many words"""
        # Generate 100x100 grid
        ROW_LENGTH = 100
        grid = self.generate_grid(ROW_LENGTH)
        ws = WordSearch(grid, ROW_LENGTH=ROW_LENGTH)

        # Generate test words
        n_words = 1000
        words = [self.generate_word(random.randint(3, 15)) 
                for _ in range(n_words)]

        # Measure search time
        start_time = time.time()
        for word in words:
            ws.is_present(word)
        end_time = time.time()

        print(f"Processed {n_words} words in {end_time - start_time:.2f} seconds")
        self.assertLess(end_time - start_time, 5.0)  # Should complete in under 5 seconds

if __name__ == '__main__':
    unittest.main()

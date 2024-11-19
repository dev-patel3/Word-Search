class WordSearch:
    def __init__(self, grid):
        """
        Initialise the word search solver with a grid.
        Args:
            grid (str): String containing the grid row by row with no separators
        """
        self.ROW_LENGTH = 100000
        self.grid = grid
        
        # Create horizontal line index for faster searching
        self.horizontal_index = {}
        for i in range(0, len(grid), self.ROW_LENGTH):
            row = grid[i:i + self.ROW_LENGTH]
            for start in range(self.ROW_LENGTH):
                # Index 3-letter prefixes for efficient filtering
                if start + 3 <= self.ROW_LENGTH:
                    prefix = row[start:start + 3]
                    if prefix not in self.horizontal_index:
                        self.horizontal_index[prefix] = []
                    # Store (row_number, column_position) for each prefix
                    self.horizontal_index[prefix].append((i // self.ROW_LENGTH, start))
        
        # Create vertical line index
        self.vertical_index = {}
        for col in range(self.ROW_LENGTH):
            for row in range(len(grid) // self.ROW_LENGTH - 2):  # -2 to ensure room for 3-letter prefix
                prefix = (
                    grid[row * self.ROW_LENGTH + col] +
                    grid[(row + 1) * self.ROW_LENGTH + col] +
                    grid[(row + 2) * self.ROW_LENGTH + col]
                )
                if prefix not in self.vertical_index:
                    self.vertical_index[prefix] = []
                self.vertical_index[prefix].append((row, col))

    def is_present(self, word):
        """
        Check if a word is present in the grid horizontally (left to right)
        or vertically (top to bottom).
        Args:
            word (str): Word to search for
        Returns:
            bool: True if word is found, False otherwise
        """
        if len(word) < 3:
            return self._brute_force_search(word)
        
        prefix = word[:3]
        
        # Check horizontal matches
        if prefix in self.horizontal_index:
            for row, col in self.horizontal_index[prefix]:
                if col + len(word) <= self.ROW_LENGTH:  # Ensure word fits
                    # Get the full potential match from the grid
                    start_pos = row * self.ROW_LENGTH + col
                    if self.grid[start_pos:start_pos + len(word)] == word:
                        return True
        
        # Check vertical matches
        if prefix in self.vertical_index:
            for row, col in self.vertical_index[prefix]:
                if row + len(word) <= self.ROW_LENGTH:  # Ensure word fits
                    # Check if full word matches
                    matches = True
                    for i in range(len(word)):
                        if self.grid[(row + i) * self.ROW_LENGTH + col] != word[i]:
                            matches = False
                            break
                    if matches:
                        return True
        
        return False
    
    def _brute_force_search(self, word):
        """
        Method for words that are shorter than 3 characters.
        """
        # Horizontal search
        for i in range(0, len(self.grid), self.ROW_LENGTH):
            row = self.grid[i:i + self.ROW_LENGTH]
            if word in row:
                return True
        
        # Vertical search
        for col in range(self.ROW_LENGTH):
            column = self.grid[col::self.ROW_LENGTH]
            if word in column:
                return True
        
        return False

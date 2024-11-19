# Word Search
## Design Approach

My optimisation strategy was to use prefix indexing to dramatically reduce the search space. Rather than scanning the entire grid for each word.

During initialisation, create indexes of all 3-letter sequences in the grid
For each search, use the word's first 3 letters to quickly locate potential matches
Only perform full word comparison at these candidate positions

This approach trades memory for speed, which is appropriate given:

-The search operation needs to be performed 1 million times

-The initialisation cost is amortized across many searches

## Key Design Decisions
### 1. Three-Letter Prefix Length
Provides good balance between index size and filtering power
With 26 possible letters, gives 17,576 possible prefixes (26³)
Long enough to be selective but short enough to work with minimum word length
Memory usage remains reasonable for a 10,000 x 10,000 grid

### 2. Data Structures
Use dictionaries for prefix indexes:

-O(1) lookup time

-Keys are 3-letter prefixes

-Values are lists of positions where prefix occurs

### 3. Position Storage
Store positions as (row, column) tuples because:

-Makes boundary checking straight-forward

-Allows for both horizontal and vertical searching

-Enables direct calculation of absolute positions when needed

### 4. Search Implementation
Two-phase search strategy:

Prefix lookup: O(1) operation to find candidate positions
Full word comparison: Only performed at candidate positions

## Space-Time Tradeoff Analysis
### Time Complexity
Initialisation: O(n²) where n is grid dimension (10,000)

Search: O(k) where k is occurrences of word's prefix

Best case: O(1) if prefix not found

Average case: Very fast due to prefix filtering

Worst case: O(n) if prefix extremely common

### Space Complexity
Grid storage: O(n²)

Prefix indexes: O(n²)

Total: O(n²)

## Alternative Approaches Considered
### Suffix Trees
I did consider using suffix trees which would make the search process much faster. But this would require excessive memory requirements for a 10,000x10,0000 grid.

## Advantage of a Multicore System
### Parallel Word Search

-Split 1 million words into chunks

-Distribute chunks across available cores

-Each core has its own copy of the index and searches independently

-Nearly linear scaling since searches are independent

-Minimal inter-process communication needed

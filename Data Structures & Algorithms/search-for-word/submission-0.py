class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row:int, col:int, word_index:int)->bool:
            if word_index== len(word)-1:
                return board[row][col]== word[word_index]
            if board[row][col]!= word[word_index]:
                return False
            original_char= board[row][col]
            board[row][col]="#"
            directions= [(-1, 0),(0,1), (1,0), (0,-1)]
            for delta_row, delta_col in directions:
                next_row= row+ delta_row
                next_col= col+ delta_col
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    board[next_row][next_col] != "#"):
                  
                    # Recursively search from the next position
                    if backtrack(next_row, next_col, word_index + 1):
                        board[row][col] = original_char  # Restore before returning
                        return True
          
            # Backtrack: restore the original character
            board[row][col] = original_char
            return False
      
        # Get board dimensions
        rows = len(board)
        cols = len(board[0])
      
        # Try starting the search from every cell in the board
        for start_row in range(rows):
            for start_col in range(cols):
                if backtrack(start_row, start_col, 0):
                    return True
      
        return False
        #Time and space complexity is O(m* n * 3^k) and O(min(n* n, k)) respectively
        #where the algorithm iterates through each cell in the m* n grid

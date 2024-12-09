import numpy as np

def load_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return np.array(grid)

def count_word_in_grid(grid, word):
    def search_word_in_direction(grid, word, delta_row, delta_col):
        word_length = len(word)
        rows, cols = grid.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                match = True
                for k in range(word_length):
                    r, c = i + k * delta_row, j + k * delta_col
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != word[k]:
                        match = False
                        break
                if match:
                    count += 1
        return count

    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Down-Right
        (-1, 1),  # Up-Right
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Up-Left
        (1, -1)   # Down-Left
    ]

    total_count = 0
    for dr, dc in directions:
        total_count += search_word_in_direction(grid, word, dr, dc)

    return total_count

if __name__ == "__main__":
    input_file = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 4\input.txt"
    word = "XMAS"
    
    grid = load_grid(input_file)
    total_occurrences = count_word_in_grid(grid, word)
    print(f"Total occurrences of '{word}': {total_occurrences}")

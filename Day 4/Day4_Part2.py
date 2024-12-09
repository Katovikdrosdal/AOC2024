def count_xmas_patterns(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    # Convert grid into a 2D list
    grid_2d = [list(row) for row in grid]

    # Grid dimensions
    rows = len(grid_2d)
    cols = len(grid_2d[0])

    # Function to check for "MAS" forward or backward
    def check_mas(sequence):
        return sequence == "MAS" or sequence == "SAM"

    # Counter for valid "X-MAS" patterns
    xmas_count = 0

    # Iterate over the grid, looking for the "X-MAS" pattern
    for i in range(1, rows - 1):  # Avoid edges for center of the X
        for j in range(1, cols - 1):  # Avoid edges for center of the X
            # Check diagonal and anti-diagonal for "MAS"
            top_left_to_bottom_right = ''.join([grid_2d[i - 1][j - 1], grid_2d[i][j], grid_2d[i + 1][j + 1]])
            bottom_left_to_top_right = ''.join([grid_2d[i + 1][j - 1], grid_2d[i][j], grid_2d[i - 1][j + 1]])
            
            # Increment count if both diagonal patterns are valid
            if check_mas(top_left_to_bottom_right) and check_mas(bottom_left_to_top_right):
                xmas_count += 1

    return xmas_count

# Usage Example
if __name__ == "__main__":
    input_file = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 4\input.txt"  # Path to your input file
    result = count_xmas_patterns(input_file)
    print(f"The X-MAS pattern appears {result} times.")

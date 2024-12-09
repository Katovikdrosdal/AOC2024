import re

def calculate_mul_sum(file_path):
    """
    Reads a file, extracts valid mul(X, Y) instructions, and calculates the sum of the results.

    Parameters:
        file_path (str): Path to the input file.

    Returns:
        int: The sum of the multiplication results.
    """
    try:
        # Read the input file
        with open(file_path, 'r') as file:
            data = file.read()

        # Define the regex pattern for valid `mul(X, Y)` instructions
        pattern = r"mul\((\d+),(\d+)\)"

        # Find all valid `mul(X, Y)` matches
        matches = re.findall(pattern, data)

        # Compute the results of the multiplications
        results = [int(x) * int(y) for x, y in matches]

        # Return the sum of all results
        return sum(results)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
if __name__ == "__main__":
    input_file_path = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 3\input.txt"
    total_sum = calculate_mul_sum(input_file_path)
    if total_sum is not None:
        print(f"The sum of all valid multiplication results is: {total_sum}")

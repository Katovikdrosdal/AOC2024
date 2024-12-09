import re

def calculate_conditional_mul_sum(file_path):
    """
    Reads a file, extracts valid mul(X, Y) instructions, and calculates the sum of the results.
    Only enabled multiplications (based on do() and don't() instructions) are considered.

    Parameters:
        file_path (str): Path to the input file.

    Returns:
        int: The sum of the results of enabled multiplications.
    """
    try:
        # Read the input file
        with open(file_path, 'r') as file:
            data = file.read()

        # Define regex patterns
        mul_pattern = r"mul\((\d+),(\d+)\)"
        control_pattern = r"(do\(\)|don't\(\))"

        # Find all control statements and `mul` instructions with their positions
        control_matches = [(match.group(), match.start()) for match in re.finditer(control_pattern, data)]
        mul_matches = [(match.group(), match.start()) for match in re.finditer(mul_pattern, data)]

        # Sort all matches by position in the data
        all_matches = sorted(control_matches + mul_matches, key=lambda x: x[1])

        # Process instructions with `do()` and `don't()` logic
        is_enabled = True  # `mul` instructions are enabled by default
        total_sum = 0

        for match, _ in all_matches:
            if match == "do()":
                is_enabled = True
            elif match == "don't()":
                is_enabled = False
            elif "mul(" in match and is_enabled:
                # Extract numbers from the `mul(X,Y)` instruction
                x, y = map(int, re.findall(r"\d+", match))
                total_sum += x * y

        return total_sum

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
if __name__ == "__main__":
    input_file_path = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 3\input.txt"
    total_sum = calculate_conditional_mul_sum(input_file_path)
    if total_sum is not None:
        print(f"The sum of all enabled multiplication results is: {total_sum}")

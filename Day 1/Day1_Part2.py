def calculate_similarity_score(file_path):
    # Read the input file and split it into two lists
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    # Calculate the similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)

    return similarity_score


if __name__ == "__main__":
    # Path to the input file
    input_file = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 1\input.txt"

    # Calculate and print the similarity score
    score = calculate_similarity_score(input_file)
    print("Similarity Score:", score)

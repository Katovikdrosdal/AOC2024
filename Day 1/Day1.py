def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for a, b in zip(left_list, right_list):
        total_distance += abs(a - b)
    return total_distance

# Read data from the input.txt file
left_list = []
right_list = []

try:
    with open(r'C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 1\input.txt', mode='r') as file:
        for line in file:
            values = line.split()
            # Assuming each line contains two space-separated numbers
            left_list.append(int(values[0]))
            right_list.append(int(values[1]))
except FileNotFoundError:
    print("Error: input.txt file not found.")
    exit()
except ValueError:
    print("Error: Ensure the input file contains only integer values.")
    exit()

# Ensure the lists are of equal length
if len(left_list) != len(right_list):
    print("Error: The two lists in the input file must have the same length.")
else:
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")


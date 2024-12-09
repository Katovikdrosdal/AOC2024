from collections import defaultdict, deque

def load_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Split the input into rules and updates
    rules_section = []
    updates_section = []
    is_update = False

    for line in lines:
        line = line.strip()
        if line == "":
            is_update = True
            continue
        if not is_update:
            rules_section.append(line)
        else:
            updates_section.append(line)

    # Parse rules into a list of tuples
    rules = []
    for rule in rules_section:
        if "|" in rule:
            x, y = map(int, rule.split("|"))
            rules.append((x, y))

    # Parse updates into a list of lists
    updates = []
    for update in updates_section:
        updates.append(list(map(int, update.split(","))))

    return rules, updates


def is_update_correct(update, rules):
    # Create a mapping from value to index for efficient lookup
    index_map = {value: i for i, value in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            # If both x and y are in the update, check the order
            if index_map[x] > index_map[y]:
                return False
    return True


def get_middle_value(update):
    middle_index = len(update) // 2
    return update[middle_index]


def topological_sort(update, rules):
    # Create adjacency list and in-degree count for the update
    adjacency_list = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            adjacency_list[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)  # Ensure all nodes appear in the in-degree map

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def main():
    # Define the path to the input file
    file_path = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 5\input.txt"

    # Load input data
    rules, updates = load_input(file_path)

    # Correctly order the incorrect updates
    middle_values = []
    for update in updates:
        if not is_update_correct(update, rules):
            sorted_update = topological_sort(update, rules)
            middle_values.append(get_middle_value(sorted_update))

    # Calculate the sum of middle values for corrected updates
    total_sum = sum(middle_values)
    print(f"Sum of middle values for corrected updates: {total_sum}")


if __name__ == "__main__":
    main()

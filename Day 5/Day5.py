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


def main():
    # Define the path to the input file
    file_path = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 5\input.txt"
    
    # Load input data
    rules, updates = load_input(file_path)

    # Find correctly ordered updates and their middle values
    middle_values = []
    for update in updates:
        if is_update_correct(update, rules):
            middle_values.append(get_middle_value(update))

    # Calculate the sum of middle values
    total_sum = sum(middle_values)
    print(f"Sum of middle values: {total_sum}")


if __name__ == "__main__":
    main()

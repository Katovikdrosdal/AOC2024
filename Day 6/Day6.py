def load_map(file_path):
    """Load the map from the input file."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def turn_right(direction):
    """Turn the guard right 90 degrees."""
    return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]

def move_forward(position, direction):
    """Move the guard one step forward."""
    x, y = position
    if direction == '^':
        return (x - 1, y)
    elif direction == 'v':
        return (x + 1, y)
    elif direction == '>':
        return (x, y + 1)
    elif direction == '<':
        return (x, y - 1)

def simulate_patrol(map_data):
    """Simulate the guard's patrol."""
    # Find the initial position and direction of the guard
    guard_position = None
    guard_direction = None
    for x, row in enumerate(map_data):
        for y, cell in enumerate(row):
            if cell in '^>v<':
                guard_position = (x, y)
                guard_direction = cell
                map_data[x][y] = '.'  # Clear the guard's initial position
                break
        if guard_position:
            break

    visited_positions = set()
    visited_positions.add(guard_position)
    rows, cols = len(map_data), len(map_data[0])

    while True:
        # Calculate the next position
        next_position = move_forward(guard_position, guard_direction)
        x, y = next_position

        # Check if the guard leaves the map
        if not (0 <= x < rows and 0 <= y < cols):
            break

        if map_data[x][y] == '#':
            # Obstacle in the way; turn right
            guard_direction = turn_right(guard_direction)
        else:
            # Move forward
            guard_position = next_position
            visited_positions.add(guard_position)

    return visited_positions

def main():
    file_path = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 6\input.txt"
    map_data = load_map(file_path)
    visited_positions = simulate_patrol(map_data)
    print("Distinct positions visited:", len(visited_positions))

if __name__ == "__main__":
    main()

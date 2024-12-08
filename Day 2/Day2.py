def is_safe(report):
    """
    Determines if a report is safe based on the given criteria:
    - Levels must be strictly increasing or strictly decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.
    """
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
        return True
    return False

def count_safe_reports(file_path):
    """
    Reads a file containing reports, determines the number of safe reports, 
    and returns the count.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count += 1
    return safe_count

if __name__ == "__main__":
    input_file = r"C:\Users\katov\OneDrive\Skrivebord\AOC2024\Day 2\input.txt"
    safe_count = count_safe_reports(input_file)
    print(f"Number of safe reports: {safe_count}")

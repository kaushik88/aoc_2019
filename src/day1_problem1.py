def parse_text_file(file_path):
    """
    Parse Text file and yield 1 line at a time.
    """
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            yield line

def calculate_fuel_required(mass):
    fuel_required = int(mass / 3) - 2
    if fuel_required <= 0:
        return 0
    return fuel_required + calculate_fuel_required(fuel_required)

def calculate_total_fuel(file_path):
    total_fuel_required = 0
    for line in parse_text_file(file_path):
        fuel_required = calculate_fuel_required(int(line))
        total_fuel_required += fuel_required
    return total_fuel_required


print(calculate_total_fuel("data/day1_problem1.txt"))
# print(calculate_fuel_required(100756))
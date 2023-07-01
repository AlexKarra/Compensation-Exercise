# 1
def calc_average(numbers: list) -> float:
    try:
        average = sum(numbers) / len(numbers)
        return average
    except (TypeError, ZeroDivisionError):
        raise ValueError('Invalid value in the list')

# Example usage:
numbers = [6, 18, 38, 42, 53]
print(calc_average(numbers))


# 2
def print_pyramid(rows):
    try:
        rows = int(rows)
    except ValueError:
        raise ValueError('Invalid value for rows')

    if rows <= 0:
        raise ValueError('Invalid value for rows')

    for line in range(rows):
        print(" " * (rows - line - 1) + '*' * (2 * line + 1))

# Example usage:
print_pyramid(24)

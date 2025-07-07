def compute_squares(nums: list[int]) -> list[int]:
    """
    Returns a list of squares of the given numbers.
    """
    return [n * n for n in nums]

# Example usage
print(compute_squares([1, 2, 3, 4, 5]))
print(compute_squares([6, 7, 8]))

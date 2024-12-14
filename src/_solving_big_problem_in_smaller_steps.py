def add_numbers(numbers):

     return sum(numbers)

    # simulate programming error - "return len(numbers)"
    #  .......assert add_numbers([1, 2, 3, 4]) == 10, "Expected sum: 10, but got a different result."


def count_numbers(numbers):
    """Returns the count of numbers in the list."""
    return len(numbers)

def divide_numbers(sum_of_numbers, count_of_numbers):
    """Returns the division of sum_of_numbers by count_of_numbers."""
    if count_of_numbers == 0:
        raise ValueError("Cannot divide by zero.")
    return sum_of_numbers / count_of_numbers

def compute_average(numbers):
    """Computes the average of the numbers by calling the existing (sub step) functions."""
    if(not numbers):
        return 0

    total = add_numbers(numbers)
    count = count_numbers(numbers)
    return divide_numbers(total, count)

##-------------------------------------
def test_add_numbers():
    print("Testing add_numbers...")
    assert add_numbers([1, 2, 3, 4]) == 10, "Expected sum: 10, but got a different result."
    assert add_numbers([0, 0, 0]) == 0, "Expected sum: 0, but got a different result."
    assert add_numbers([-1, -2, -3]) == -6, "Expected sum: -6, but got a different result."
    assert add_numbers([]) == 0, "Expected sum: 0 for an empty list."
    print("All add_numbers tests passed.\n")


def test_count_numbers():
    print("Testing count_numbers...")
    assert count_numbers([1, 2, 3, 4]) == 4, "Expected count: 4, but got a different result."
    assert count_numbers([0, 0, 0]) == 3, "Expected count: 3, but got a different result."
    assert count_numbers([-1, -2, -3]) == 3, "Expected count: 3, but got a different result."
    assert count_numbers([]) == 0, "Expected count: 0 for an empty list."
    print("All count_numbers tests passed.\n")


def test_divide_numbers():
    print("Testing divide_numbers...")
    assert divide_numbers(10, 2) == 5.0, "Expected division result: 5.0, but got a different result."
    assert divide_numbers(0, 5) == 0.0, "Expected division result: 0.0, but got a different result."
    assert divide_numbers(-10, 2) == -5.0, "Expected division result: -5.0, but got a different result."

    try:
        divide_numbers(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero.", "Expected a ValueError for division by zero."
    else:
        assert False, "Expected a ValueError when dividing by zero, but no exception was raised."
    print("All divide_numbers tests passed.\n")


### Tests for `compute_average`

def test_compute_average():
    print("Testing compute_average...")
    assert compute_average([1, 2, 3, 4]) == 2.5, "Expected average: 2.5, but got a different result."
    assert compute_average([10, 20, 30]) == 20.0, "Expected average: 20.0, but got a different result."
    assert compute_average([-1, -2, -3]) == -2.0, "Expected average: -2.0, but got a different result."
    assert compute_average([100]) == 100.0, "Expected average: 100.0, but got a different result."
    assert compute_average([]) == 0, "Expected average: 0 for an empty list."
    print("All compute_average tests passed.\n")
# Run tests
def test_functions():
    test_add_numbers()
    test_count_numbers()
    test_divide_numbers()
    test_compute_average()

def main():
    nums = (1,3,8)
    av = compute_average(nums)
    print(f"average of {nums} is {av}")

if __name__ == "__main__":
    test_functions()   # All add_numbers tests passed......All compute_average tests passed.
    main()              # average of (1, 3, 8) is 4.0

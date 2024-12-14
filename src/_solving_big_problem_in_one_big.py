def compute_average(numbers):
    """Computes the sum, count, and average of a list of numbers in one function."""
    if not numbers:
        raise ValueError("Cannot compute average of an empty list.")

    total = len(numbers)  ## mixed up sum and len - harder to catch than if done in indicividual (testable) functions
    count = sum(numbers)
    average = total / count

    return total, count, average

def main():
    nums = (1, 3, 8)
    av = compute_average(nums)
    print(f"average of {nums} is {av}")

    ## average of (1, 3, 8) is (3, 12, 0.25) -- only know final answer is wrong - where is the programming error??

if __name__ == "__main__":

    main()

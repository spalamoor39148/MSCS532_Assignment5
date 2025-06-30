import time
import random
import sys
import matplotlib.pyplot as plt # Import matplotlib.pyplot

# Increase the recursion depth limit (use with caution)
sys.setrecursionlimit(2000)

# ... (rest of the quicksort, randomized_quicksort, and iterative_quicksort functions as before)



def quicksort(arr, low, high):
    """
    Quicksort algorithm using the last element as the pivot.
    """
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort the sub-arrays
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    """
    Partitions the array around a pivot (last element).
    """
    pivot = arr[high]  # Choose the last element as the pivot
    i = (low - 1)  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to its correct position
    return (i + 1)

import random

def randomized_partition(arr, low, high):
    """
    Randomly selects a pivot and partitions the array around it.
    """
    pivot_index = random.randint(low, high)  # Randomly select a pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap the pivot with the last element
    return partition(arr, low, high)  # Partition the array using the original partition function

def randomized_quicksort(arr, low, high):
    """
    Implements the recursive Randomized Quicksort algorithm.
    """
    if low < high:
        # p is the partitioning index, arr[p] is now at the right place
        p = randomized_partition(arr, low, high)

        # Recursively sort the left and right subarrays
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)







############################


def generate_random_array(size):
    return [random.randint(0, size * 10) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def run_experiment(sort_func, arr_type, size, num_trials=5):
    total_time = 0
    for _ in range(num_trials):
        if arr_type == 'random':
            arr = generate_random_array(size)
        elif arr_type == 'sorted':
            arr = generate_sorted_array(size)
        elif arr_type == 'reverse_sorted':
            arr = generate_reverse_sorted_array(size)

        arr_copy = arr[:]
        start_time = time.time()
        
        # Call the appropriate sorting function
        if sort_func == quicksort:
            quicksort(arr_copy, 0, len(arr_copy) - 1)
        elif sort_func == randomized_quicksort:
            randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)

        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / num_trials

# Experiment settings
input_sizes = [1000, 2000, 3000, 4000, 5000] # Adjust as needed for your machine
distributions = ['random', 'sorted', 'reverse_sorted']

# Store results
results = {dist: {'deterministic': [], 'randomized': []} for dist in distributions}

print("--- Quicksort Performance Comparison ---")

for size in input_sizes:
    print(f"\nInput Size: {size}")
    for dist in distributions:
        print(f"  Distribution: {dist}")

        # Deterministic Quicksort
        print(f"    Deterministic Quicksort:")
        try:
            det_time = run_experiment(quicksort, dist, size)
            results[dist]['deterministic'].append(det_time)
            print(f"      Time: {det_time:.6f} seconds")
        except RecursionError:
            print("      RecursionError: maximum recursion depth exceeded")
            results[dist]['deterministic'].append(float('inf')) # Represent RecursionError with infinity

        # Randomized Quicksort
        print(f"    Randomized Quicksort:")
        rand_time = run_experiment(randomized_quicksort, dist, size)
        results[dist]['randomized'].append(rand_time)
        print(f"      Time: {rand_time:.6f} seconds")


# Plot the results
for dist in distributions:
    plt.figure()
    plt.plot(input_sizes, results[dist]['deterministic'], label='Deterministic Quicksort', marker='o')
    plt.plot(input_sizes, results[dist]['randomized'], label='Randomized Quicksort', marker='x')
    
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Quicksort Performance on {dist.capitalize()} Data")
    plt.legend()
    plt.grid(True)
    plt.show() # Display the plot

    # Optional: Save the plot to a file
    # plt.savefig(f"quicksort_performance_{dist}.png")

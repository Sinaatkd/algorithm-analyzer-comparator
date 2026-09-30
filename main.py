import time
import tracemalloc


# ==========================================
# Algorithm 1: Linear Search
# ==========================================
def algorithm_1(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# ==========================================
# Algorithm 2: Binary Search
# ==========================================
def algorithm_2(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# ==========================================
# Run Algorithm and Measure Performance
# ==========================================
def measure_algorithm(algorithm, *args):

    tracemalloc.start()

    start_time = time.perf_counter()

    result = algorithm(*args)

    end_time = time.perf_counter()

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "result": result,
        "time": end_time - start_time,
        "memory": peak_memory
    }


# ==========================================
# Compare Two Algorithms
# ==========================================
def compare_algorithms(algorithm1, algorithm2, *args):

    result1 = measure_algorithm(algorithm1, *args)
    result2 = measure_algorithm(algorithm2, *args)

    print("\n" + "=" * 50)
    print("ALGORITHM COMPARISON PLATFORM")
    print("=" * 50)

    # ------------------------------------------
    # Compare Outputs
    # ------------------------------------------
    print("\n1. FUNCTIONAL COMPARISON")
    print("-" * 50)

    print("Algorithm 1 Output:", result1["result"])
    print("Algorithm 2 Output:", result2["result"])

    if result1["result"] == result2["result"]:
        print("\nResult: Both algorithms do the SAME job.")
    else:
        print("\nResult: Algorithms produce DIFFERENT outputs.")

    # ------------------------------------------
    # Time Comparison
    # ------------------------------------------
    print("\n2. TIME COMPARISON")
    print("-" * 50)

    print(
        f"Algorithm 1 Execution Time: "
        f"{result1['time']:.10f} seconds"
    )

    print(
        f"Algorithm 2 Execution Time: "
        f"{result2['time']:.10f} seconds"
    )

    if result1["time"] < result2["time"]:
        print("\nAlgorithm 1 is faster.")

    elif result2["time"] < result1["time"]:
        print("\nAlgorithm 2 is faster.")

    else:
        print("\nBoth have similar execution time.")

    # ------------------------------------------
    # Memory Comparison
    # ------------------------------------------
    print("\n3. MEMORY COMPARISON")
    print("-" * 50)

    print(
        f"Algorithm 1 Peak Memory: "
        f"{result1['memory']} bytes"
    )

    print(
        f"Algorithm 2 Peak Memory: "
        f"{result2['memory']} bytes"
    )

    if result1["memory"] < result2["memory"]:
        print("\nAlgorithm 1 uses less memory.")

    elif result2["memory"] < result1["memory"]:
        print("\nAlgorithm 2 uses less memory.")

    else:
        print("\nBoth use similar memory.")

    print("\n" + "=" * 50)


# ==========================================
# Main
# ==========================================
if __name__ == "__main__":

    # Test Data
    data = list(range(1, 100001))

    target = 99999

    compare_algorithms(
        algorithm_1,
        algorithm_2,
        data,
        target
    )

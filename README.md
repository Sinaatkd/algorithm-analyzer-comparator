Algorithm Comparison Platform

A simple Python platform for comparing two algorithms based on their output, execution time, and memory usage.

The goal of this project is to provide an easy way to test whether two algorithms produce the same result and compare their performance.

Features

- Compare two Python algorithms
- Check whether both algorithms produce the same output
- Measure execution time
- Measure peak memory usage
- Determine which algorithm is faster
- Determine which algorithm uses less memory
- Simple single-file implementation
- No external libraries required

Project Structure

algorithm-comparison/
│
├── main.py
└── README.md

Requirements

- Python 3.8 or newer

The project only uses Python standard libraries:

- "time"
- "tracemalloc"

Therefore, no additional packages need to be installed.

How It Works

The program receives two Python functions:

algorithm_1()
algorithm_2()

Both algorithms are executed using the same input.

The platform then compares them in three stages.

1. Functional Comparison

The outputs of both algorithms are compared:

result1 == result2

If the results are equal, the program reports that both algorithms produced the same output for the tested input.

«Note: Producing the same result for one or more test inputs does not mathematically prove that two algorithms are equivalent for every possible input.»

2. Execution Time

Execution time is measured using:

time.perf_counter()

The program reports the execution time of each algorithm and determines which one was faster during the test.

3. Memory Usage

Memory usage is measured using Python's:

tracemalloc

The program records the peak memory usage of each algorithm and compares the results.

Example

The default example compares Linear Search and Binary Search.

Algorithm 1 — Linear Search

def algorithm_1(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

Algorithm 2 — Binary Search

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

Running the Project

Clone or download the project and run:

python main.py

Or:

python3 main.py

Example Output

==================================================
ALGORITHM COMPARISON PLATFORM
==================================================

1. FUNCTIONAL COMPARISON
--------------------------------------------------
Algorithm 1 Output: 99998
Algorithm 2 Output: 99998

Result: Both algorithms do the SAME job.

2. TIME COMPARISON
--------------------------------------------------
Algorithm 1 Execution Time: 0.0301421000 seconds
Algorithm 2 Execution Time: 0.0000092000 seconds

Algorithm 2 is faster.

3. MEMORY COMPARISON
--------------------------------------------------
Algorithm 1 Peak Memory: 156 bytes
Algorithm 2 Peak Memory: 128 bytes

Algorithm 2 uses less memory.

==================================================

Actual execution time and memory usage may be different depending on the computer, Python version, operating system, and current system load.

Using Your Own Algorithms

Replace "algorithm_1" and "algorithm_2" inside "main.py" with the algorithms you want to compare.

For example:

def algorithm_1(data):
    # First algorithm
    return result


def algorithm_2(data):
    # Second algorithm
    return result

Then provide the test input:

compare_algorithms(
    algorithm_1,
    algorithm_2,
    data
)

Both algorithms should accept compatible inputs and return comparable outputs.

Example Complexity Comparison

For the included search example:

Algorithm| Time Complexity| Space Complexity
Linear Search| O(n)| O(1)
Binary Search| O(log n)| O(1)

These are the theoretical complexities of the algorithms.

The current platform measures actual runtime and peak memory consumption; it does not automatically derive theoretical Big-O complexity from source code.

Limitations

The current version has several limitations:

- It compares algorithms using provided test inputs.
- Equal outputs on tested inputs do not prove complete algorithm equivalence.
- Execution time can vary between runs.
- Memory measurements can vary depending on the Python runtime.
- Theoretical Big-O complexity is not automatically detected.
- Binary Search requires sorted input.

Future Improvements

Possible improvements include:

- Run algorithms multiple times and calculate average execution time
- Automatically generate test cases
- Test different input sizes
- Estimate empirical time complexity
- Estimate empirical memory complexity
- Detect patterns such as "O(1)", "O(log n)", "O(n)", "O(n log n)", and "O(n²)"
- Generate performance charts
- Add a graphical user interface
- Allow users to enter algorithms dynamically
- Export comparison reports

Purpose

This project is intended for educational use and demonstrates basic concepts related to:

- Algorithm analysis
- Time complexity
- Space complexity
- Performance benchmarking
- Functional comparison

License

This project is available for educational and personal use.

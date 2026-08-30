# Task 09: Matrix Multiplication Showdown

## Overview

This task implements matrix multiplication using three different algorithms:

1. Naive Matrix Multiplication
2. Divide and Conquer Matrix Multiplication
3. Strassen's Matrix Multiplication

The program accepts two matrices from the user, calculates their product using all three algorithms, measures the execution time of each method, and verifies that all three methods produce the same result.

## Algorithms Used

### 1. Naive Matrix Multiplication

The naive method uses three nested loops.

For every element in the result matrix, it multiplies the corresponding elements of a row of Matrix A and a column of Matrix B and adds them together.

Time Complexity: `O(n³)`

Space Complexity:`O(n²)` for the result matrix.

### 2. Divide and Conquer

The Divide and Conquer method divides each matrix into four smaller submatrices.

The smaller matrices are recursively multiplied and the resulting submatrices are combined to form the final matrix.

Time Complexity:`O(n³)`

Space Complexity:`O(n²)` for storing the matrices and results.

### 3. Strassen's Algorithm

Strassen's algorithm also divides the matrices into smaller submatrices, but reduces the number of recursive matrix multiplications from eight to seven.

It uses additional matrix additions and subtractions to calculate the final result.

Time Complexity: `O(n^log₂7)` ≈ `O(n²·⁸⁰⁷)`

Space Complexity:`O(n²)` approximately, excluding recursive temporary storage.

## Benchmarking Approach

The Python time.perf_counter() function is used to measure the execution time of each algorithm.

The process is:

1. Start the timer.
2. Execute the matrix multiplication algorithm.
3. Stop the timer.
4. Calculate the elapsed time.
5. Display the execution time in seconds.

The program also compares the results produced by all three algorithms to verify their correctness.

Example output:


=== Execution Time ===
Naive:            0.00001711 seconds
Divide & Conquer: 0.00003297 seconds
Strassen:         0.00004372 seconds

=== Verification ===
All three algorithms produced the same result.


The execution time can vary depending on the matrix size and the computer being used.

## Input Validation

The program checks whether matrix multiplication is possible.

The number of columns in Matrix A must be equal to the number of rows in Matrix B.

For example:


A = 2 × 3
B = 3 × 2


These matrices can be multiplied.

The program also validates that the correct number of elements is entered for each row.

## Padding

Divide and Conquer and Strassen's algorithms work most conveniently when the matrix dimensions can be divided recursively.

Therefore, the program pads the matrices with zeros to the next suitable power-of-two size before applying these algorithms.

The extra zero elements are removed from the final result.

## Challenges Faced

* Implementing recursive matrix multiplication correctly.
* Dividing matrices into four submatrices.
* Combining the resulting submatrices correctly.
* Implementing Strassen's seven multiplication operations.
* Handling matrices whose dimensions are not powers of two.
* Making sure all three algorithms produce exactly the same result.
* Measuring very small execution times accurately.

## Concepts Learned

* Matrix multiplication
* Recursion
* Divide and Conquer
* Strassen's algorithm
* Time complexity
* Space complexity
* Benchmarking algorithms
* Python functions and lists
* Input validation
* Matrix padding
* Performance comparison
* Result verification

## Resources Used

* Python documentation
* Algorithms and data structures concepts
* Matrix multiplication concepts
* Divide and Conquer algorithm concepts
* Strassen's matrix multiplication algorithm
* Python `time` module and `time.perf_counter()`

## Sample Test

### Matrix A

1 2
3 4


### Matrix B


5 6
7 8


### Output


19 22
43 50

All three algorithms produced the same result.

## Conclusion

The task successfully demonstrates three different approaches to matrix multiplication. The program verifies the correctness of the algorithms and compares their execution times, providing practical experience with recursion, algorithm design, complexity analysis, and benchmarking.

## File Structure:
~~~
/LAB _01/
├── exercise1_integer_mirror.xx (xx is dependent of the used programming language)
├── exercise2_balanced_symbols.xx
├── exercise3_merge_intervals.xx
├── exercise4_polynomial_eval.xx
├── exercise5_array_rotation.xx
├── exercise6_first_unique.xx
└── README.md (Team members and assigned exercises, Brief description of each solution, Complexity analysis summary)
~~~

---

## Team members and assigned exercises
Team: T14

Yuefan LIU: 1, 4

Mouzheng LI: 2, 5

Xinyue LI: 3, 6

---

## Dependencies and Language version
Please use **python 3.11 or higher version**

Please use **JDK 17 or a higher version**.

---

## Instructions

For using Java programme: 

**Exercise 1 — Integer Mirror — Usage (Java)**

Input format:

* One non-negative integer `n`

Output:

* The integer obtained by reversing the decimal digits of `n` (no string conversion)

Example:

* Input:

  * `315`
* Output:

  * `513`

Additional examples:

* Input: `0` → Output: `0`
* Input: `400` → Output: `4`

**Exercise 4 — Polynomial Evaluation (Horner) — Usage (Java)**

Input format:

* First line: `m` (number of coefficients)
* Second line: `m` real numbers `a0 a1 ... a(m-1)` where `ai` is the coefficient of `x^i`
* Last line: `x` (real number)

Example:

* Input:

  * `4`
  * `3 -2 0 5`
  * `2.0`
* Output:

  * `39.0`


---

##  Brief description of each solution

### Solution of exercise2_balanced_symbols

The function is_balanced(s) checks whether a string "s" containing parentheses "()", brackets "[]", and braces "
{}" is balanced using a stack-based approach. Each opening symbol is pushed onto the stack, and each closing symbol is matched with the most recent opening symbol. If a mismatch occurs or the stack is empty when a closing symbol is found, the function returns False; otherwise, it returns True when the stack is empty at the end of the traversal. The function also counts and returns the number of comparisons performed during execution.

### Solution of exercise5_array_rotation

This exercise implements three different methods to rotate an array to the right by k positions. RotateTemp uses an auxiliary array to place each element at its rotated position before copying it back, RotateOneByOne performs the rotation step by step by repeatedly shifting elements to the right, and RotateReverse applies the reversal technique by reversing the entire array and then reversing the first k elements and the remaining elements separately. These approaches demonstrate different trade-offs between time complexity and additional memory usage.

### Solution of exercise3_merge_intervals

The but of this exercise is to practice sorting and interval manipulation algorithms.The approach is to first sort the intervals by their starting values. Then, iterate through the list, comparing each interval with the previous one. If the intervals overlap, merge them by updating their ending values. If they don't overlap, store the previous interval and continue processing the next.This way, after sorting, only one iteration is needed to obtain the final merged list.

### Solution of exercise6_first_unique

The but of this exercise is to practice hash table/dictionary usage for frequency counting.First, we use a dictionary to count how many times each character appears. Then we go through the string again and return the index of the first character whose count is 1. If no such character exists, we return -1.
This method is simple and efficient because we only scan the string twice.

### Solution of exercise1_integer_mirror

This program reverses the decimal digits of a non-negative integer using only arithmetic operations (mod, div, multiplication and addition). No string conversion is used.

Example:

```
Input: 315
Output: 513
```

The algorithm extracts the last digit using `n % 10`, appends it to the result using
`result = result * 10 + digit`, and removes the last digit using integer division
`n = n / 10`. The process continues until `n = 0`.

---

### Solution of exercise4_polynomial_eval

This program evaluates a polynomial using Horner’s method.

Given:

```
P(x) = a0 + a1x + a2x^2 + ... + anx^n
```

The polynomial is evaluated in nested form:

```
(((an)x + a(n-1))x + ... )x + a0
```

Instead of computing powers of x separately, the algorithm starts from the highest-degree coefficient and repeatedly multiplies the current result by x and adds the next coefficient. This eliminates exponentiation and reduces the total number of multiplications.

Test cases (edge cases):

```
coeffs = [3, -2, 0, 5], x = 2.0  → 39.0
coeffs = [7], x = 2.5           → 7.0
coeffs = [0, 0, 0], x = 10      → 0.0
coeffs = [1, 1, 1], x = 0       → 1.0
coeffs = [1, -1, 1], x = -1     → 3.0
```


---

## Complexity analysis summary

### Complexity of exercise2_balanced_symbols

For the balanced symbols problem, the algorithm scans the input string once and performs constant-time stack operations for each character, resulting in a **time complexity of O(n)** where n is the length of the string, and a **space complexity of O(n)** in the worst case when all symbols are opening brackets.

### Complexity of exercise5_array_rotation

For the array rotation problem, 

**RotateTemp** runs in **O(n) time** with **O(n) additional space** due to the auxiliary array;

**RotateOneByOne** runs in **O(n × k) time**, in the worst case is **O(n^2) time**, since it shifts elements one position at a time but uses **O(1) extra space**;

**RotateReverse** runs in **O(n) time** because each element is moved a constant number of times while only requiring **O(1) additional space**.


### Complexity of exercise3_merge_intervals

The time complexity is O(n log n).
The sorting step takes O(n log n) time.After sorting, we only scan the list once to merge intervals, which takes O(n) time.
So the total time complexity is O(n log n).
The space complexity is O(n) in the worst case, when no intervals overlap.

### Complexity of exercise6_first_unique

The time complexity is O(n).
We scan the string twiceEach step takes O(n) time. So the total time complexity is O(n).
The space complexity is also O(n) in the worst case if all characters are different.

### Complexity of exercise1_integer_mirror

For a d-digit number, the loop runs d times.
Each iteration performs:

* 1 mod
* 1 div
* 1 multiplication
* 1 addition

So the total number of operations is proportional to 4d, which gives:

Time complexity: O(d)

Since the number of digits d is equal to ⌊log10(n)⌋ + 1,
the time complexity in terms of n is:

O(log n)

The space complexity is O(1) because only a few variables are used.



### Complexity of exercise4_polynomial_eval

For a degree-n polynomial, the algorithm processes each coefficient once.
Each iteration performs:

* 1 multiplication
* 1 addition

So the total number of operations is proportional to 2n.

Time complexity: O(n)

### Comparison with naive approach

The naive approach computes powers explicitly, such as:

x², x³, ..., xⁿ

To compute these powers, repeated multiplications are required.
If powers are recomputed for each term, the total number of multiplications can grow quadratically in the worst case.

Horner’s method avoids this by rewriting the polynomial in nested form.
It eliminates exponentiation and keeps the computation strictly linear.

Time complexity remains O(n).

Space complexity is O(1) because only one auxiliary variable (result) is used.


---

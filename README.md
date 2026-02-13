# Dependencies and Language version
Please use Java 8 or a higher version.

# Brief description of each solution


## Solution of exercise1_integer_mirror

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

## Solution of exercise4_polynomial_eval

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

# Complexity analysis summary

## Complexity of exercise1_integer_mirror

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



## Complexity of exercise4_polynomial_eval

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





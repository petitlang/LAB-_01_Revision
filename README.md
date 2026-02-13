# LAB-_01_Revision

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

---

##  Brief description of each solution

### Solution of exercise2_balanced_symbols

The function is_balanced(s) checks whether a string "s" containing parentheses "()", brackets "[]", and braces "
{}" is balanced using a stack-based approach. Each opening symbol is pushed onto the stack, and each closing symbol is matched with the most recent opening symbol. If a mismatch occurs or the stack is empty when a closing symbol is found, the function returns False; otherwise, it returns True when the stack is empty at the end of the traversal. The function also counts and returns the number of comparisons performed during execution.

### Solution of exercise5_array_rotation

This exercise implements three different methods to rotate an array to the right by k positions. RotateTemp uses an auxiliary array to place each element at its rotated position before copying it back, RotateOneByOne performs the rotation step by step by repeatedly shifting elements to the right, and RotateReverse applies the reversal technique by reversing the entire array and then reversing the first k elements and the remaining elements separately. These approaches demonstrate different trade-offs between time complexity and additional memory usage.

---

## Complexity analysis summary

### Complexity of exercise2_balanced_symbols

For the balanced symbols problem, the algorithm scans the input string once and performs constant-time stack operations for each character, resulting in a **time complexity of O(n)** where n is the length of the string, and a **space complexity of O(n)** in the worst case when all symbols are opening brackets.

### Complexity of exercise5_array_rotation

For the array rotation problem, 

**RotateTemp** runs in **O(n) time** with **O(n) additional space** due to the auxiliary array;

**RotateOneByOne** runs in **O(n × k) time**, in the worst case is **O(n^2) time**, since it shifts elements one position at a time but uses **O(1) extra space**;

**RotateReverse** runs in **O(n) time** because each element is moved a constant number of times while only requiring **O(1) additional space**.

---

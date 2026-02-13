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

### Solution of exercise3_merge_intervals

The but of this exercise is to practice sorting and interval manipulation algorithms.The approach is to first sort the intervals by their starting values. Then, iterate through the list, comparing each interval with the previous one. If the intervals overlap, merge them by updating their ending values. If they don't overlap, store the previous interval and continue processing the next.This way, after sorting, only one iteration is needed to obtain the final merged list.

### Solution of exercise6_first_unique

The but of this exercise is to practice hash table/dictionary usage for frequency counting.First, we use a dictionary to count how many times each character appears. Then we go through the string again and return the index of the first character whose count is 1. If no such character exists, we return -1.
This method is simple and efficient because we only scan the string twice.

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


---

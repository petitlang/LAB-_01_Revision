


# Dependencies and Language version
Please use python 3.11 or higher version.
Please use JDK 17 or a higher version.

# Instructions
Input format:

One line string message

The string may contain letters, spaces, punctuation.

Only ! and ? are considered as urgency punctuation.

Type exit to terminate the program.

Output:

The program prints:

Number of uppercase letters

Number of punctuation marks (! and ?)

Caps ratio (uppercase / alphabetic characters)

Classification: CALM / URGENT / AGGRESSIVE

Whether there exists a character repeated more than 3 consecutive times

Classification Rules:

AGGRESSIVE

capsRatio ≥ 0.6
OR

punctuation ≥ 5

URGENT

capsRatio ≥ 0.3
OR

punctuation ≥ 3

CALM

Otherwise

Examples
Example 1

Input:

HELLO!!!

Output:

Uppercase: 5
Punctuation: 3
Caps ratio: 1.00
Classification: AGGRESSIVE
Repeat>3: false

# Solution of exercise1_classify_message 

This solution analyzes a friend request message by scanning the string character by character.

The algorithm counts:

* the number of uppercase letters
* the number of alphabetic characters
* the number of urgency punctuation marks ('!' and '?')

It also detects whether a character is repeated more than three consecutive times by comparing each character with its predecessor and maintaining a run-length counter.

After the scan:

* The caps ratio is computed as:

[capsRatio = upperCount / alphaCount]

(If alphaCount = 0, capsRatio is defined as 0 to avoid division by zero.)

The message is then classified as:

* **AGGRESSIVE** if capsRatio ≥ 0.6 OR punctuation ≥ 5
* **URGENT** if capsRatio ≥ 0.3 OR punctuation ≥ 3
* **CALM** otherwise

The algorithm uses only constant extra variables and processes the string in a single traversal.

---

# Complexity of exercise1_classify_message

Let ( n ) be the length of the message.

To detect consecutive repeated characters, adjacent characters are compared:

[C(n) = n - 1]

since the first character has no predecessor.

Therefore:

[C(n) ∈ Θ(n)]

All required computations are performed during one traversal of the string:

[Minimal passes = 1]

Any correct solution must inspect each character at least once:

[T(n) >= n]

Thus:

[T(n) ∈ Θ(n)]

If Unicode characters beyond ASCII are supported, the traversal remains linear:

[T(n) = c' * n]

where ( c' > c ) due to more complex character classification.

The asymptotic complexity does not change; only the constant factor increases.

Space complexity:

[S(n) ∈ Θ O(1)]

since only a fixed number of counters and variables are used.

---



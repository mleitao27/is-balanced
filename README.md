# is-balanced
Python script that checks if an expression is balanced regarding brackets: '()', '[]' and '{}'. The script asks the user to input the expression to be evaluated and outputs eiter 'Balanced' if the expression is in fact balanced or 'Not Balanced at <number>' where <number> matches position of the bracket that unbalances the expression.

## Problem
Check for Balanced Brackets in an expression (well-formedness)
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.
  
Example:
  
Input: exp = “[()]{}{[()()]()}”
Output: Balanced
  
Input: exp = “[(])”
Output: Not Balanced


## Usage
Run:
```
$ python main.py
```
  
## Data structures
I used a stack to store tuples with the opening brackets and their position in the expression. As the script goes through the expression it stacks the opening brackets and when it find the closing brackets pops the last opening bracket inserted in the stack.
  
## Big O notation
O(N), where N is the size of the expression.

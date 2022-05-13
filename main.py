#!/usr/bin/python

import sys

def isBalanced(exp):
    # Balanced flag
    balanced = True
    # stack to store opening brackets
    stack = []
    # Index of the current exp char
    index = 0
    # Index where exp is unbalanced
    unbalancedIndex = -1
    for i in exp:
        index += 1
        # Add opening brackets to stack
        if i == '(' or i == '[' or i == '{':
            stack.append((i, index))
        # Ignore other chars
        elif(i != ')' and i != ']' and i != '}'):
            continue
        # Check if closing brackets match opening ones
        else:
            # If opening brackets in stack
            if len(stack) > 0:
                aux = stack[len(stack) - 1]
                stack.pop()
                if aux[0] == '(' and i != ')':
                    unbalancedIndex = aux[1]
                    balanced = False
                    break
                if aux[0] == '[' and i != ']':
                    unbalancedIndex = aux[1]
                    balanced = False
                    break
                if aux[0] == '{' and i != '}':
                    unbalancedIndex = aux[1]
                    balanced = False
                    break
            # Closing brackets before opening
            else:
                unbalancedIndex = index
                balanced = False
                break
    # Not matched opening brackets left in stack
    if len(stack) > 0:
        if(unbalancedIndex == -1):
            unbalancedIndex = stack[len(stack) - 1][1]
        balanced = False
    
    # Print answer
    if balanced:
        print('Balanced')
    else:
        print('Not Balanced at ' + str(unbalancedIndex))

def main():
    exp = input('Insert expression> ')
    isBalanced(exp)

if __name__ == '__main__':
    main()
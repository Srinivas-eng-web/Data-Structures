"""
what is stack ?
LIFO principle : Last In Lirst Out
core operations : push ,pop,peek,isempty
-> Think of stack of plates ,you always
add on top  (push)
remove from top (pull)
"""
#Stack Implementation in Python
stack = []
#push
stack.append(10)
print(stack) # output : [10]

stack.append(20)
print(stack) #output: [10, 20]

stack.append(30)
stack.append(40)
stack.append(50)
print(stack) #output : [10, 20, 30, 40, 50]

#pop
print(stack.pop()) #output : 50

#peek
print(stack[-1]) #output : 40

#isempty

print(len(stack) == 0) # output : False --> because we have an elements in the stack right

#Better way: collections.deque

from collections import deque
stack = deque()
stack.append(10)
stack.append(20)

print(stack.pop()) #output : 20
print(stack[-1]) #10
print(len(stack)==0) # False
# Why deque?  Because list.pop() from end is fine, but deque is optimized
# for both ends(more efficient in large-scale ops).

# Reverse using stack

def revese_string(s):
    stack = []
    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string
result = revese_string("Srinivasa Reddy")
print(result) #yddeR asavinirS

# Clear LIFO behavior (good for explaining to interviewers).
# Better conceptual fit for reversal.
# Time complexity is closer to O(n) (though still not ideal due to string concat in loop).
# Minor cons: Uses extra memory (stack list).
s = "srinivasa"
result = ""
for i in s:
    result = i + result
print(result)
#pros : simple and readable , No extra data structures
#cons : Inefficient for large strings, result = i + result creates a new string every time, causing O(n²) time complexity due to repeated copying.

s = "srini"
result = "".join(reversed(s))
print(result)

# Problem: Valid Parentheses
# given a string of brackets like "({[]})". You need to check if:
# Every opening bracket has a matching closing bracket
# The brackets are properly nested and closed in the right order
def valid_parentheses(s):
    stack = []
    mapping = {')':"(","]":"[" ,"}":"{" }
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
result = valid_parentheses(s="([{}])")
print(result)  #output : True

def valid_parenthises(s):
    stack = []
    mapping = {")":"(","[":"]","{":"}"}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack and stack.pop != mapping[char]
                return False
    return not stack


#Reverse polish Notation
""" why RPN ?
instead of 3+4 infix(normal math) in RPN ,we write 3 4 +
and for (2+3) *4  in RPN 2 3 + 4 * -> add 2+3 ,then multiply result by 4
why use RPN ?
->No need parentheses
->Easy to evaluate using stack
->Efficient for computers and compilers

RPN evaluation logic(high level)
1.use stack
2.scan each token (number & operator) from the left
3.if it's a number push it into the stack 
4.if its operator an opertor 
-> pop the top 2 numbers
-> Apply the operation
->push the result back on to the stack
5.At the end , the stack will contain the one result

"""

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
            print(f"pushed number {token} -> stack :{stack}")
        else:
            b = stack.pop()
            a = stack.pop()
            print(f"operator : {token} operands :{a} ,{b}")

            if token == "+":
                result = a+b
            elif token == "-":
                result = a-b
            elif token == "*":
                result =  a*b
            elif token == "/":
                result = int(a/b)

            stack.append(result)
    return stack[0]

print(eval_rpn(tokens=["2", "1", "+", "3", "*"]))

#Next Greater Element (NGE)
#Given an array,for each element find the next element to its right if none exists,return -1

def next_greater_brute(nums):
    result = []
    for i in range(len(nums)):
        found = False
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                result.append(nums[j])
                found = True
                break
            if not found:
                result.append(-1)
    return result
print(next_greater_brute(nums= [4, 5, 2, 10]))


#using stack
#1.use stack to store indices whose next greater elements haven't been found yet
#2.Traverse the list from right to left
#3.POP smaller elements from the stack
#4.the top of the stack is the next greater

def next_greater_element(nums):
    stack = []
    result = [0]*len(nums)
    for i in range(len(nums)-1,-1,-1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()
        #if stack has elements ,that has the next greater
        result[i] = stack[-1] if stack else -1

        #push the current element into the stack
        stack.append(nums[i])

    return result
output = next_greater_element(nums=[4,5,2,10])
print(output)



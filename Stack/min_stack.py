'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

# Beats 88.88% in runtime, beats 32.52% in memory 

# Technique: Dynamically programmed stack of potential minimum elems
# ex. stack: [2,3,1,9,7,-2,5,8,0,-6]
# potential min_so_far or min_after_pops stack = [2, 1, -2, -6]

# Reason: 3 for ex. can never be a min as it is higher on the stack than an elem 2 which is less than it

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_so_far = []
        

    def push(self, val: int) -> None:
        if self.min_so_far == [] or val <= self.min_so_far[-1]:
            self.min_so_far.append(val)
        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        if self.stack[-1] == self.min_so_far[-1]:
            self.min_so_far = self.min_so_far[:-1]
        self.stack = self.stack[:-1]
        return None

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_so_far[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


# initialize the stack
stack = Stack()
# use push to add a '1' to the stack
stack.push(1)
# Check to see if stack 'is_empty' should return false here
print('1 -> ', stack.is_empty())
# Print the current list of items in your stack
print('2 -> ', stack.items, "<-- Current Stack")
# Use 'pop' to remove the top number from the stack
item = stack.pop()
# Print the item that you have just removed from the stack, stored in 'item'
print('3 -> ', item)
# Check to see if stack 'is_empty' should return true after 'pop'
print('4 -> ', stack.is_empty(), '\n\n\n')

# Create a second stack 'stack2'
stack2 = Stack()
# Use 'for' loop to append numbers 0-5
for i in range(0, 6):
    stack2.push(i)
# Printh the current list of items in your stack
print('5 -> ',stack2.items)
# Use 'peek' to check the top item on your stack
print('6 -> ', stack2.peek())
# Use 'size' to get the number of items in your stack
print('7 -> ', stack2.size())
stack2.pop()
stack2.pop()
print(stack2.size())

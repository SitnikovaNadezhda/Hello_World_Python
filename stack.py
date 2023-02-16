stack = [i for i in range(10)]
print(*stack)

stack.append(100)
stack.append(101)
print(stack.pop())
print(stack[-1])

print(*stack)

while stack:
    print(stack.pop())
